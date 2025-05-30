import cv2

# Load main image and template
image = cv2.imread('C:/Users/vijay/Documents/One Drive/OneDrive/Pictures/Screenshots/Screenshot 2025-05-14 001007.png')
template = cv2.imread('C:/Users/vijay/Documents/One Drive/OneDrive/Pictures/Screenshots/Screenshot 2025-05-14 001007.png', 0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Template Matching
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# Draw rectangle
w, h = template.shape[::-1]
cv2.rectangle(image, max_loc, (max_loc[0]+w, max_loc[1]+h), (0,255,0), 2)

cv2.imshow('Detected Watch', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
