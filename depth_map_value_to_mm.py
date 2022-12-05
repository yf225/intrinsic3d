import cv2

iphone13pro_mm_to_negated_value_ratio = 1.8527918781725887

def depth_map_value_to_mm(depth_map_value_file_path):
    depth_map_value_np = cv2.imread(depth_map_value_file_path)
    cv2.imwrite(depth_map_value_file_path.replace(".depth.original.png", ".depth.png"), (256 - depth_map_value_np) * iphone13pro_mm_to_negated_value_ratio)

if __name__ == "__main__":
    import sys
    depth_map_value_to_mm(sys.argv[1])