#!/usr/bin/env python3


import sys
import numpy as np
import matplotlib.pyplot as plt
from util import *

__author__ = "Hunter Chasens"
__license__ = "GPLv3"
__version__ = "0.1"
__email__ = "hunter.chasens18@ncf.edu"


def pcaPercent(data, percent=80):
    assert(percent <= 100 and percent >= 0)
    (norm, mean, std) = Utils.z_score(data, False)      #1. Normalize by Z-Score
    (pc, eig) = Utils.getPC(norm)                #2. Calculate Principal Components
    y = norm @ pc                                #3. Rotate onto Principal Components
    pc_percent = (eig/np.sum(eig))*100               # Here we find the percentage of each Principal Component
    d = 0
    sum = 0
    for x in pc_percent:
        sum += x
        d+=1
        if sum > percent:
            break
    y_proj = y[:,0:d]                            #4. Project onto the d-dimensional subspace defined by the first d principal component
    data_rec = (y_proj @ pc[:,0:d].T)*std + mean #5. Reconstruct
    return data_rec

def pca(data, d=2):
    (norm, mean, std) = Utils.z_score(data, False)      #1. Normalize by Z-Score
    pc = Utils.getPC(norm)                #2. Calculate Principal Components
    y = norm @ pc                                #3. Rotate onto Principal Components
    y_proj = y[:,0:d]                            #4. Project onto the d-dimensional subspace defined by the first d principal component
    data_rec = (y_proj @ pc[:,0:d].T)*std + mean #5. Reconstruct
    return data_rec

def TDExample(data):
    #plt.imshow(data[9,:,:])
    plt.imshow(pcaPercent(data[8,:,:]))

if __name__=="__main__":
    #iris = Utils.parse("./data/iris.data")
    #lfw = Utils.parse("./data/lfwcrop.npy") 
    optRaw = Utils.parse("./data/optdigits.tra")
    #optdigits require some processing
    optclass = optRaw[:, -1]        #we save the class
    opt = optRaw[:, :-1]             #then split off the class
    opt = opt.reshape(3823, 8, 8)
    TDExample(opt)

    plt.show()