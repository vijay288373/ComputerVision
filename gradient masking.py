import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg', cv2.IMREAD_GRAYSCALE)

# Sobel operator
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine gradients
gradient = cv2.magnitude(sobelx, sobely)
gradient = np.clip(gradient, 0, 255).astype(np.uint8)

plt.imshow(gradient, cmap='gray')
plt.title('Gradient Sharpening')
plt.axis('off')
plt.show()
