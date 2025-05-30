import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Load image in grayscale
image_path = r"C:\Users\vijay\Downloads\butterfly1.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Step 3: Create the unsharp mask
unsharp_mask = cv2.subtract(image, blurred)

# Step 4: Add the mask back to the original to get the sharpened image
sharpened = cv2.add(image, unsharp_mask)

# Step 5: Display results
plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(1, 4, 2), plt.imshow(blurred, cmap='gray'), plt.title('Blurred')
plt.subplot(1, 4, 3), plt.imshow(unsharp_mask, cmap='gray'), plt.title('Unsharp Mask')
plt.subplot(1, 4, 4), plt.imshow(sharpened, cmap='gray'), plt.title('Sharpened')
plt.tight_layout()
plt.show()
