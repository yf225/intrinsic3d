import cv2

def depth_map_value_to_mm(depth_map_value_file_path):
    depth_map_value_np = cv2.imread(depth_map_value_file_path)
    cv2.imwrite(depth_map_value_file_path.replace(".depth.original.png", ".depth.png"), 256 - depth_map_value_np)

if __name__ == "__main__":
    import sys
    depth_map_value_to_mm(sys.argv[1])