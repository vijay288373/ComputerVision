import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Read the image (convert to grayscale)
image = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg', cv2.IMREAD_GRAYSCALE)

# Step 2: Define Laplacian kernel with diagonal neighbors
laplacian_kernel = np.array([[1, 1, 1],
                             [1, -8, 1],
                             [1, 1, 1]])

# Step 3: Apply the Laplacian kernel
laplacian_result = cv2.filter2D(image, -1, laplacian_kernel)

# Step 4: Sharpen the image
sharpened_image = cv2.add(image, laplacian_result)

# Step 5: Show the images
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(1, 3, 2), plt.imshow(laplacian_result, cmap='gray'), plt.title('Laplacian Output')
plt.subplot(1, 3, 3), plt.imshow(sharpened_image, cmap='gray'), plt.title('Sharpened')
plt.show()
