import cv2
import numpy as np

# Load image
image = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg', 0)

# Convert to binary
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# Display result
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
