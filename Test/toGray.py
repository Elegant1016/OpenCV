from skimage.color import rgb2gray
from skimage import io
from skimage.viewer import ImageViewer
from skimage.exposure import equalize_hist
import numpy as np

image = io.imread("lady.jpg")
gray_image = rgb2gray(image)

viewer = ImageViewer(image)
viewer.show()

viewer = ImageViewer(gray_image)
viewer.show()

equalized_image = equalize_hist(gray_image)
viewer = ImageViewer(equalized_image)
viewer.show()

binary_image = np.where(gray_image > np.mean(gray_image),1.0,0.0)
viewer = ImageViewer(binary_image)
viewer.show()

# io.imsave('test_16bit.jpg', binary_image)
# io.imsave('test_16bit.jpg', binary_image, plugin='pil')
io.imsave('test_16bit.jpg', equalized_image, plugin='pil')

print ("Colored image shape:\n", image.shape)
print ("Grayscale image  shape:\n", gray_image.shape)

