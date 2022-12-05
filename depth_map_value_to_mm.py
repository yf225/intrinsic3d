import cv2
import numpy as np


iphone13pro_mm_to_negated_value_ratio = 1.8527918781725887  # From physical measurement

# depth map value file is the original depth image file from iPhone HEIC image after heif-convert extraction

def depth_map_value_to_mm(depth_map_value_file_path):
    depth_map_value_np = cv2.imread(depth_map_value_file_path)
    # depth_map_mm_np = ((256 - depth_map_value_np) * iphone13pro_mm_to_negated_value_ratio).astype(np.float16)
    depth_map_mm_np = (256 - depth_map_value_np) * iphone13pro_mm_to_negated_value_ratio
    cv2.imwrite(depth_map_value_file_path.replace(".depth.original.png", ".depth.png"), depth_map_mm_np)

if __name__ == "__main__":
    import sys
    depth_map_value_to_mm(sys.argv[1])