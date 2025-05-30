import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\vijay\Downloads\butterfly1.jpeg")  # Updated path with raw string

# Check if the image is loaded
if image is None:
    print("Error: Image not loaded. Check the file path.")
    exit()

# Define the Laplacian kernel (with negative center coefficient)
laplacian_kernel = np.array([[0,  1,  0],
                              [1, -4,  1],
                              [0,  1,  0]])

# Apply the Laplacian filter
sharpened_image = cv2.filter2D(image, -1, laplacian_kernel)

# Save or display the sharpened image
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
