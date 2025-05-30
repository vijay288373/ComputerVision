import cv2
import numpy as np

# Load image
image = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg', 0)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply closing
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display result
cv2.imshow('Closed Image', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
