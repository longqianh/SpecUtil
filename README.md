# SpecUtil
Metrics, Algorithms for Hyperspectral Reconstruction.



## Metrics

- Mean relative absolute error
  $$
  \text{MRAE}=\frac{1}{n}\left\|\frac{\mathbf{x}-\hat {\mathbf x}}{\mathbf{x}}\right\|_1
  $$
  

- Goodness of fit coefficient 
  $$
  \text{GFC}=\frac{\mathbf x}{|\mathbf x|}\cdot\frac{\hat{\mathbf{x}}}{|\hat{\mathbf x}|}
  $$
  

- Root mean square error
  $$
  \text{RMSE}=\sqrt{\frac{1}{n}\|\mathbf{x}-\hat{\mathbf{x}}\|}
  $$

- Peak signal-to-noise ratio
  $$
  \text{PSNR}=20\times\log_{10}\left(\frac{v_{\max}}{\text{RMSE}}\right)
  $$
  $v_{\max}$ is the maximum possible value for the pixel.

