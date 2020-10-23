# PCA Example

Principal Components Analysis Real World Example - Project 4 Report for Machine Learning

## Overview

### Description

An example of Principal Component Analysis to reduce the dimensionality of datasets. Three test datasets are used, `Iris`, `Optdigits`, and `LFW Crop`. They're placed in a `/data` directory which is under `.gitignore`. As such they are not uploaded to this repository. All data has been preprocessed by removing all strings.
> Notice: This code base is not maintained. Many things are hard code. The code in this repository was strictly used for created the graphics for this report and **is not intended to be forked or reused.** It may be used for reference within the confines of the license.

### Algorithm

The Basics

1. Normalize by Z-Score <div style="text-align: right"><img src="https://render.githubusercontent.com/render/math?math=\hat{x} = \frac{X-\mu}{\sigma }"><div>
2. Calculate Principal Components <div style="text-align: right"> ![PCA of a multivariate Gaussian distribution](https://upload.wikimedia.org/wikipedia/commons/f/f5/GaussianScatterPCA.svg) Order in decreasing value the eigenvalues of the covariance matrix<div> 

3. Rotate onto Principal Components <div style="text-align: right"><img src="https://render.githubusercontent.com/render/math?math=Y=XP"><div>
4. Project onto the d-dimensional subspace defined by the first d principal component <div style="text-align: right"><img src="https://render.githubusercontent.com/render/math?math=Y[:,0:d]"><div> 
5. Reconstruct <div style="text-align: right"><img src="https://render.githubusercontent.com/render/math?math=X^*=(YP^T)\sigma +\mu "><div> 

## Report
There are three parts to this report. Each part includes an eigenvector heatmap, a scaled eigenvector scree plot, and reconstructions of four stages of data retention. The Optdigits and LFW Crop sections include the showcase of random images alongside a data retention showcase.
### Part I - Iris
#### Iris Raw ![IrisRaw](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/iris/irisRaw.png)
#### Iris PCA Scree Map ![IrisScree](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/iris/IrisScree.png)
#### Eigenvalue Heatmap ![EiganHeatmap](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/iris/IrisEigenHeatmap.png)
#### Iris Red Vs Blue
Iris Raw - Blue
Iris 25% PCA - Red
For this graph I tried to use contrasting colors but I think red overtook blue. That and because blue holds more detail it might not be able to stand its ground visually against red 20% PCA.
![RedVBlue](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/iris/IrisRawBlue25Red.png)
#### Iris at 80% retension used  2  dimensions.
#### Iris: percent =  20  d =  1 ![Iris20](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/iris/Iris20.png)
At d = 1 this holds 25% of our data. It clearly still hold enough to identify Irises.
#### Iris: percent =  40  d =  1 ![Iris40](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/iris/Iris40.png)
#### Iris: percent =  60  d =  1 ![Iris60](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/iris/Iris60.png)
#### Iris: percent =  80  d =  2 ![Iris80](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/iris/Iris80.png)

### Part II - Optdigits
Sample taken = 0

#### Octdigit Raw ![OctRaw](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/optdigits/OptRaw.png)
#### Oct PCA Scree Map ![OctScree](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/optdigits/OptScree.png)
#### Eigenvalue Heatmap ![EiganHeatmap](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/optdigits/OptEigenHeatmap.png)

#### Optdigits at 80% retension used  2  dimensions.
#### Optdigits: percent =  20  d =  1 ![Opt20](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/optdigits/Opt20.png)
#### Optdigits: percent =  40  d =  1 ![Opt40](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/optdigits/Opt40.png)
#### Optdigits: percent =  60  d =  1 ![Opt60](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/optdigits/Opt60.png)
#### Optdigits: percent =  80  d =  2 ![Opt80](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/optdigits/Opt80.png)

### Part III - LFW Crop 
Sample taken = 0
#### LFW Raw ![LFWRaw](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/lfwcrop/LFWRaw.png)
#### LFW PCA Scree Map ![LFWScree](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/lfwcrop/LFWScree.png)
#### Eigenvalue Heatmap ![EiganHeatmap](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/lfwcrop/LFWEigenHeatmap.png)


#### lfw at 80% retension used  4  dimensions.
#### lfw: percent =  20  d =  1 ![LFWRaw](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/lfwcrop/LFW20.png)
#### lfw: percent =  40  d =  2 ![LFWRaw](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/lfwcrop/LFW40.png)
#### lfw: percent =  60  d =  3 ![LFWRaw](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/lfwcrop/LFW60.png)
#### lfw: percent =  80  d =  4 ![LFWRaw](https://raw.githubusercontent.com/hchasens/PCA-Example/main/figures/lfwcrop/LFW80.png)


## Licensing

GNU General Public License v3.0
