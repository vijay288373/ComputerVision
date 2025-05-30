import cv2, numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg', cv2.IMREAD_GRAYSCALE)
A = 1.5
lap = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
highpass = cv2.filter2D(img, -1, lap)
highboost = np.clip(A*img - highpass, 0, 255).astype(np.uint8)

plt.figure(); plt.imshow(highboost, cmap='gray'); plt.title('High-Boost (A=1.5)'); plt.axis('off')
plt.show()
