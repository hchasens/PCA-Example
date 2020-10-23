# PCA Example

Principal Components Analysis Real World Example

## Overview

### Description

An example of Principal Component Analysis to reduce the dimensionality of datasets. Three test datasets are used, `Iris`, `Optdigits`, and `LFW Crop`. They're placed in a `/data` directory which is under `.gitignore`. As such they are not uploaded to this repository. All data has been preprocessed by removing all strings.

### Algorithm

The Basics

1. Normalize by Z-Score <div style="text-align: right"><img src="https://render.githubusercontent.com/render/math?math=\hat{x} = \frac{X-\mu}{\sigma }"><div>
2. Calculate Principal Components <div style="text-align: right"> ![PCA of a multivariate Gaussian distribution](https://upload.wikimedia.org/wikipedia/commons/f/f5/GaussianScatterPCA.svg) Order in decreasing value the eigenvalues of the covariance matrix<div> 

3. Rotate onto Principal Components <div style="text-align: right"><img src="https://render.githubusercontent.com/render/math?math=Y=XP"><div>
4. Project onto the d-dimensional subspace defined by the first d principal component <div style="text-align: right"><img src="https://render.githubusercontent.com/render/math?math=Y[:,0:d]"><div> 
5. Reconstruct <div style="text-align: right"><img src="https://render.githubusercontent.com/render/math?math=X^*=(YP^T)\sigma +\mu "><div> 

## Licensing

GNU General Public License v3.0
