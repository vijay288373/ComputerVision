import cv2
import numpy as np

# Load image
image = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg', 0)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display result
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
