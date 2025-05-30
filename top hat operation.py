import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load grayscale image
image = cv2.imread(r'C:\Users\vijay\Downloads\butterfly1.jpeg', cv2.IMREAD_GRAYSCALE)

# Define kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

# Perform Top Hat operation
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Display result
plt.imshow(tophat, cmap='gray')
plt.title('Top Hat Operation')
plt.axis('off')
plt.show()
