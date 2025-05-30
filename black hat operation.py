import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load grayscale image
image = cv2.imread(r'C:\Users\vijay\Downloads\butterfly1.jpeg', cv2.IMREAD_GRAYSCALE)

# Define kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

# Perform Black Hat operation
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Display result
plt.imshow(blackhat, cmap='gray')
plt.title('Black Hat Operation')
plt.axis('off')
plt.show()
