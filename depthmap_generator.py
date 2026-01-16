import cv2
import numpy as np
import os

def generate_depth_map(left_image_path, right_image_path, output_disparity_path):
    
    # Taking input images
    if not os.path.exists(left_image_path) or not os.path.exists(right_image_path):
        raise FileNotFoundError("One or both of the input image paths do not exist.")

    img_left = cv2.imread(left_image_path)
    img_right = cv2.imread(right_image_path)

    if img_left is None or img_right is None:
        raise ValueError("Could not read one or both of the input images.")

    # Convert images to grayscale
    gray_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

    # Create StereoSGBM object (more accurate but slower)
    stereo = cv2.StereoSGBM_create(
        minDisparity=0,
        numDisparities=96,
        blockSize=5,
        P1=8 * 3 * 5**2,
        P2=32 * 3 * 5**2,
        disp12MaxDiff=1,
        uniquenessRatio=10,
        speckleWindowSize=100,
        speckleRange=32
    )

    # Compute the disparity map
    disparity = stereo.compute(gray_left, gray_right).astype(np.float32)

    # Normalize the disparity values
    # Disparity can have negative values, so we normalize to 0..255 for display
    disp_min = disparity.min()
    disp_max = disparity.max()

    # Avoid division by zero if everything is the same color or disparity is constant
    if disp_max - disp_min == 0:
        disp_max = disp_min + 1

    disparity_normalized = cv2.normalize(
        disparity, 
        None, 
        alpha=0, 
        beta=255, 
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_8U
    )

    # Apply a color map to the normalized disparity
    
    disparity_color = cv2.applyColorMap(disparity_normalized, cv2.COLORMAP_JET)

    # Save the resulting color disparity map
    cv2.imwrite(output_disparity_path, disparity_color)

    # Return the colorized disparity in case further processing is needed
    return disparity_normalized

def main():
    left_img_path = "images/left.png"    
    right_img_path = "images/right.png"
    output_path = "depth.png" 
    
    # Generate depth map
    depth_map_color = generate_depth_map(left_img_path, right_img_path, output_path)

    img_left = cv2.imread(left_img_path)
    img_right = cv2.imread(right_img_path)

    cv2.imshow("Left Image", img_left)
    cv2.imshow("Right Image", img_right)
    cv2.imshow("Depth Map (Color)", depth_map_color)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
