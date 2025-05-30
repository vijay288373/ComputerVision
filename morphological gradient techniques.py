import cv2
import numpy as np

# Load image
image = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg', 0)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply morphological gradient
gradient_image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Display result
cv2.imshow('Morphological Gradient Image', gradient_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
