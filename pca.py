#!/usr/bin/env python3


import sys
import numpy as np
import matplotlib.pyplot as plt
from util import *

__author__ = "Hunter Chasens"
__license__ = "GPLv3"
__version__ = "0.1"
__email__ = "hunter.chasens18@ncf.edu"


def pca(data, d=2, percent=0):
    """[performs PCA, dimensions xor percent may be used. If both are used then percent will override dimensions.]

    Args:
        data ([nparray]): [data]
        d (int, optional): [description]. Defaults to 2.
        percent (int, optional): [description]. Defaults to 0.

    Returns:
        [type]: [description]
    """

    (norm, mean, std) = Utils.z_score(data, False)      #1. Normalize by Z-Score
    (pc, eig) = Utils.getPC(norm)                #2. Calculate Principal Components
    y = norm @ pc                                #3. Rotate onto Principal Components
    y_proj = y[:,0:d]                            #4. Project onto the d-dimensional subspace defined by the first d principal component
    data_rec = (y_proj @ pc[:,0:d].T)*std + mean #5. Reconstruct

    #plt.plot(data[:,0], data[:,1], 'or')
    #plt.plot(data_rec[:,0], data_rec[:,1], 'o')
    return data_rec

def TDExample(data):
    #plt.imshow(data[0,:,:])
    plt.imshow(pca(data[0,:,:]))

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