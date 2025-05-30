import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = r"C:\Users\vijay\Downloads\butterfly.jpeg"
image = cv2.imread(image_path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the points for the perspective transformation
# Original points (you can adjust these based on your image)
points_original = np.float32([[100, 100], [400, 100], [100, 300], [400, 300]])
# Corresponding points in the transformed image
points_transformed = np.float32([[0, 0], [500, 0], [0, 400], [500, 400]])

# Get the perspective transformation matrix
matrix = cv2.getPerspectiveTransform(points_original, points_transformed)

# Apply the perspective transformation
transformed_image = cv2.warpPerspective(rgb_image, matrix, (500, 400))

# Display the original and transformed images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(rgb_image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Transformed Image')
plt.imshow(transformed_image)
plt.axis('off')

plt.show()
