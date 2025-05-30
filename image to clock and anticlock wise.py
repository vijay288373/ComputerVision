import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = r"C:\Users\vijay\Downloads\sample_house.jpg"
image = cv2.imread(image_path)

# Convert from BGR to RGB for displaying correctly in matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rotate 90 degrees clockwise
rotated_cw = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate 90 degrees counter-clockwise
rotated_ccw = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Convert rotated images to RGB
rotated_cw_rgb = cv2.cvtColor(rotated_cw, cv2.COLOR_BGR2RGB)
rotated_ccw_rgb = cv2.cvtColor(rotated_ccw, cv2.COLOR_BGR2RGB)

# Display all three images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Clockwise Rotation")
plt.imshow(rotated_cw_rgb)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Counter-Clockwise Rotation")
plt.imshow(rotated_ccw_rgb)
plt.axis('off')

plt.tight_layout()
plt.show()
