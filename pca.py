#!/usr/bin/env python3


import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from util import *

__author__ = "Hunter Chasens"
__license__ = "GPLv3"
__version__ = "0.1"
__email__ = "hunter.chasens18@ncf.edu"


def pcaPercent(data, percent=80):
    """[PCA by Percent]

    Args:
        data ([nparray]): [input data]
        percent (int, optional): [percent of information retention]. Defaults to 80.

    Returns:
        [nparray]: [nparray containing Principle Components with the <percent> information retained]
    """
    assert(percent <= 100 and percent >= 0)
    (norm, mean, std) = Utils.z_score(data, False)      #1. Normalize by Z-Score
    (pc, eig) = Utils.getPC(norm)                #2. Calculate Principal Components
    y = norm @ pc                                #3. Rotate onto Principal Components
    scaled_eig = (eig/np.sum(eig))*100               # Here we find the percentage of each Principal Component
    d = 0
    sum = 0
    for x in scaled_eig:
        sum += x
        d+=1
        if sum > percent:
            break
    y_proj = y[:,0:d]                            #4. Project onto the d-dimensional subspace defined by the first d principal component
    data_rec = (y_proj @ pc[:,0:d].T)*std + mean #5. Reconstruct
    return data_rec, eig, scaled_eig, d

def pca(data, d=2):
    """[PCA]

    Args:
        data ([nparray]): [input data]
        d (int, optional): [dimensional subspace to keep]. Defaults to 2.

    Returns:
        [nparray]: [nparray containing Principle Components with the highest information retained up to <d> dimensions]
    """
    (norm, mean, std) = Utils.z_score(data, False)      #1. Normalize by Z-Score
    (pc, eig) = Utils.getPC(norm)                #2. Calculate Principal Components
    y = norm @ pc                                #3. Rotate onto Principal Components
    y_proj = y[:,0:d]                            #4. Project onto the d-dimensional subspace defined by the first d principal component
    data_rec = (y_proj @ pc[:,0:d].T)*std + mean #5. Reconstruct
    return data_rec, eig

def TDExample(data):
    #plt.imshow(data[9,:,:])
    #plt.imshow(data[5,:,:])
    #plt.show()
    #plt.imshow(pca(data[5,:,:], 3))
    #plt.imshow(pcaPercent(np.mean(data,axis=0), 50)[0])
    #heatmap(pcaPercent(data[0,:,:])[1])
    #screeplot(pcaPercent(np.mean(data,axis=0), 50)[2])
    #plt.show()
    #plt.imshow(np.mean(data,axis=0))
    #plt.show()
    #plt.imshow(pcaPercent(np.mean(data,axis=0), 25) @ np.mean(data,axis=0))
    pass

def report():
    """ 

    Part I: Iris
    Part II: Optdigits
    Part III: LFW Crop

    Visualize the sorted eigenvectors with a heatmap, with labeled axes.
    Visualize the sorted, scaled eigenvalues with a scree plot.

    How many dimensions are required in the projection in order to retain 80% of the information in the dataset?
    Visualize the rotated dataset as a 2D scatterplot by  projecting onto the first 2 principal components.
    Reconstruct the dataset following several different projections with at least 4 different varying degrees of information retention
    For Iris: Visualize the original (raw) and reconstructed data in 2 different colors in the same 2D scatterplot. Use petal length as the X axis and petal width as the Y axis. 

    For Optdigits and LFW Crop: There are no original features that it's helpful to project onto. Instead:
        Pick any sample (row) from the original dataset. You can choose it randomly, or find your favorite :)
        Visualize your chosen sample as a heatmap with plt.imshow().
        Then rotate your sample into PC-space (Y_sample = X[ row, : ] @ P), and
        project it onto the first d PCs -- where d is however many it takes to retain approximately 25%, 50%, 75%, and then 100% of the data.
        Visualize each of these reconstructions as a heatmap, alongside the original.
        Explain in your report: What happens to the appearance of these reconstructions as you retain more dimensions?
    
    """ 
    #Part I - Iris
    iris = Utils.parse("./data/iris.data")
    """
    Visualize the sorted eigenvectors with a heatmap, with labeled axes.
    Visualize the sorted, scaled eigenvalues with a scree plot.
    How many dimensions are required in the projection in order to retain 80% of the information in the dataset?
    

    pca = pcaPercent(iris, 80)  #returns data_rec, eig, scaled_eig, d
    #heatmap(pca[1])
    #screeplot(pca[2])
    print("Iris at 80% retension used ", pca[3], " dimensions.")

   
    Visualize the rotated dataset as a 2D scatterplot by  projecting onto the first 2 principal components.
    Reconstruct the dataset following several different projections with at least 4 different varying degrees of information retention
    For Iris: Visualize the original (raw) and reconstructed data in 2 different colors in the same 2D scatterplot. Use petal length as the X axis and petal width as the Y axis. 
    """
    #sns.heatmap(iris, cmap='Blues')
    #sns.heatmap(pcaPercent(iris, 25)[0], cmap='Reds')
    #plt.show()
    """
    sns.heatmap(pcaPercent(iris, 20)[0])
    print()
    plt.show() 
    sns.heatmap(pcaPercent(iris, 50)[0])
    plt.show()
    sns.heatmap(pcaPercent(iris, 70)[0])
    plt.show()
    sns.heatmap(pcaPercent(iris, 100)[0])
    plt.show()
    sns.heatmap(iris)

    for x in range(20,100, 20):
        pca = pcaPercent(iris, x)
        sns.heatmap(pca[0])
        print("Iris: percent = ", x, " d = ", pca[3])
        plt.show()
    """
    optRaw = Utils.parse("./data/optdigits.tra")
    #optdigits require some processing
    optclass = optRaw[:, -1]        #we save the class
    opt = optRaw[:, :-1]             #then split off the class
    opt = opt.reshape(3823, 8, 8)  
    """
    pca = pcaPercent(opt[0,:,:], 80)
    pca = pcaPercent(iris, 80)  #returns data_rec, eig, scaled_eig, d
    #heatmap(pca[1])
    #screeplot(pca[2])
    print("Iris at 80% retension used ", pca[3], " dimensions.") 
    for x in range(20,100, 20):
        pca = pcaPercent(opt[0,:,:], x)
        plt.imshow(pca[0])
        print("Opt: percent = ", x, " d = ", pca[3])
        plt.show()
    """
    lfw = Utils.parse("./data/lfwcrop.npy")  
    pca = pcaPercent(lfw[0,:,:], 80)
    
    #heatmap(pca[1])
    #screeplot(pca[2])
    #print("lfw at 80% retension used ", pca[3], " dimensions.") 
    """
    for x in range(20,100, 20):
        pca = pcaPercent(lfw[0,:,:], x)
        plt.imshow(pca[0])
        print("lfw: percent = ", x, " d = ", pca[3])
        plt.show()
    """
    plt.imshow(lfw[0,:,:])
    plt.show()
    plt.imshow(opt[0,:,:])


def heatmap(eig):
    sns.heatmap(eig.reshape(-1, 1))
    title_obj = plt.title('Eigenvalues Heatmap')
    plt.setp(title_obj, color='k')
    plt.pause(0.1)

def screeplot(scaled_eig):
    fig, ax = plt.subplots( 2, 1 )
   
    cumulated = np.cumsum(scaled_eig)
    ax[0].plot(scaled_eig, '-o')
    ax[1].plot(cumulated, '-o')
   
    ax[0].set_title( "Percent of information retained by individual PCs" )
    ax[0].set_ylim([-5, 110])
    ax[0].grid( True )
 
    ax[1].set_title( "Cumulative information retained by all PCs" )
    ax[1].set_ylim([-5, 110])
    ax[1].grid( True )
    #both subplots share this label
    ax[1].set_ylabel("persent of retained information")
    ax[1].set_xlabel("Principle Componet")
    plt.show()


if __name__=="__main__":
    report()
    plt.show()