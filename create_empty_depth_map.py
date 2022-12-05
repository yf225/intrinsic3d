import cv2
import numpy as np


def create_empty_depth_map(color_image_file_path, example_depth_map_value_file_path):
    depth_map_value_np = cv2.imread(example_depth_map_value_file_path).fill(0)
    cv2.imwrite(color_image_file_path.replace(".png", ".depth.png"), depth_map_value_np)

if __name__ == "__main__":
    import sys
    depth_map_value_to_mm(sys.argv[1], sys.argv[2])