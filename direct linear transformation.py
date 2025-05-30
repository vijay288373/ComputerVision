import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_homography_dlt(src_pts, dst_pts):
    """
    Compute homography matrix using Direct Linear Transformation (DLT) method.
    :param src_pts: Nx2 array of source points
    :param dst_pts: Nx2 array of destination points
    :return: 3x3 homography matrix
    """
    n = src_pts.shape[0]
    if n < 4:
        raise ValueError("At least 4 points required")

    A = []
    for i in range(n):
        x, y = src_pts[i]
        u, v = dst_pts[i]
        A.append([-x, -y, -1, 0, 0, 0, x*u, y*u, u])
        A.append([0, 0, 0, -x, -y, -1, x*v, y*v, v])
    A = np.array(A)

    # Solve Ah=0 by SVD
    U, S, Vh = np.linalg.svd(A)
    L = Vh[-1, :]
    H = L.reshape(3, 3)

    # Normalize so that H[2,2] = 1
    H /= H[2, 2]
    return H

def main():
    image_path = r"C:\Users\vijay\Downloads\butterfly.jpeg"
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read image from the path.")
        return

    height, width = img.shape[:2]

    # Define 4 source points from the image - select manually as an example
    src_pts = np.array([
        [100, 100],
        [width - 100, 100],
        [100, height - 100],
        [width - 100, height - 100]
    ], dtype=np.float32)

    # Define 4 destination points - mapping to a rectangle of desired size
    dst_pts = np.array([
        [0, 0],
        [width, 0],
        [0, height],
        [width, height]
    ], dtype=np.float32)

    # Compute homography matrix using DLT
    H = compute_homography_dlt(src_pts, dst_pts)

    # Apply the perspective transformation
    transformed_img = cv2.warpPerspective(img, H, (width, height))

    # Convert BGR to RGB for plotting with matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    transformed_rgb = cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB)

    # Plot original and transformed images
    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img_rgb)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Transformed Image using DLT')
    plt.imshow(transformed_rgb)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
