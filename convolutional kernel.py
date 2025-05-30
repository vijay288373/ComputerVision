import cv2
import numpy as np
# Load image
image = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg', 0)
# Define Sobel kernel
sobel_kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
# Apply convolution
edges = cv2.filter2D(image, -1, sobel_kernel)
# Threshold the result
_, boundary_image = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)
# Display result
cv2.imshow('Boundary Image', boundary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
