""" Contains utility classes.

"""

import numpy as np

__author__ = "Hunter Chasens"
__license__ = "GPLv3"
__version__ = "0.1"
__email__ = "hunter.chasens18@ncf.edu" 


class Utils:
    """[Uninstantiated class that contains utility functions.]
    """

    @staticmethod
    def getPC(normdata):
        """[Returns the order principle compoenets of a dataset. Principle compoenets are order from by their eigenvalues from greatest to least.]

        Args:
            normdata ([nparray]): [data to be processed]

        Returns:
            [nparray, nparray]: [principle compoenets sorted by corresponding eigenvalues from greatest to least, ordered eigenvalues]
        """
        covmrx = np.cov(normdata,rowvar=False)      #creates a coverance matrix out of the normalized data
        (eigvals, pc) = np.linalg.eig(covmrx)       #find the eigenvalues and all unsorted principle compoenets
        order = np.argsort(eigvals)[::-1]           #finds the order from greatest to least of the eigenvalues
        eigvals = eigvals[order]                    #rearranges the eigenvalues from greatest to least
        pc = pc[:, order]                           #rearranges all principle compoenets such that their corresponding eigenvalues are order from greatest to least
        return pc, eigvals

    @staticmethod
    def z_score(data, removeOutliers=True):
        """[normalizes an nparray by z-score (e.g. normalizes all features by standard deviation such that the standard deviation of any feature is 1)]

        Args:
            data ([nparray]): [the nparray to be normalized]
            removeOutliers ([Boolean]): [removes outliers greater then three standard deviations]


        Returns:
            [nparray]: [a Z-Scored normalized nparray]
            [int]: [original mean of data]
            [int]: [original standard deviation of data]

        """
        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0)      # while using the optdigits.tra dataset I found (after hours of debugging) that my 
        #Here we are removing the row in which std is zero, meaning all data in that colum is the same. I'm sure there's a cleaner way of doing this and will research it.
        mean = mean[std != 0]
        data = data[:, std != 0]
        std = std[std != 0]             #we must do std last to preserve the original structure for the other's boolean indexing
        zscore = ( data - mean ) / std  # I keep getting a bug here, I think its because some std values are 0 so its trying to divide by zero
        if removeOutliers == True:
            zscore = zscore[np.any(zscore < 3*std, axis=1)]
        return zscore, mean, std

    @staticmethod
    def parse(filename):
        """[Converts diffrent files into nparrays. Does not take headers. Only CSVs, TRA, and NPY files as of Alpha]

        Args:
            filename ([String]): [filepath to data, must include filename and extension]

        Returns:
            [nparray]: [the parsed datafile]
        """
        arr = np.empty
        if (".npy" in filename):
            print("reading npy")
            arr = np.load(filename)
        else:
            print("reading csv")
            arr = np.genfromtxt(filename, delimiter=',')
            arr = arr[~np.isnan(arr).any(axis=1)]
        return arr
