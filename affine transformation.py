import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\vijay\Downloads\butterfly.jpeg"
image = cv2.imread(image_path)

# Get the dimensions of the image
rows, cols, _ = image.shape

# Define the points for the affine transformation
# Original points
points_original = np.float32([[50, 50], [200, 50], [50, 200]])
# Transformed points
points_transformed = np.float32([[10, 100], [200, 50], [100, 250]])

# Get the affine transformation matrix
matrix = cv2.getAffineTransform(points_original, points_transformed)

# Apply the affine transformation
transformed_image = cv2.warpAffine(image, matrix, (cols, rows))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
