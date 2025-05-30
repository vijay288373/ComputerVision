import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Load the image (convert to grayscale)
image_path = r'C:\Users\vijay\Downloads\butterfly1.jpeg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Define Laplacian kernel with positive center
laplacian_kernel = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

# Step 3: Apply the kernel
sharpened_image = cv2.filter2D(image, -1, laplacian_kernel)

# Step 4: Display images
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(sharpened_image, cmap='gray'), plt.title('Sharpened with +5 center')
plt.show()
