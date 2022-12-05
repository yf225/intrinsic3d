"""
r11, r12, r13, tx
r21, r22, r23, ty
r31, r32, r33, tz
0, 0, 0, 1

Dest Example:
0.999988 0.00191916 -0.00456571 0.001998
-0.00193682 0.999991 -0.00386558 0.004864
0.00455825 0.00387438 0.999982 0.000162
0 0 0 1

Source Example:
5.6883312837103635 -0.42095354602526996 2.3249676160538435 0.99670428579834358 -0.017586608837283815 -0.079191400169577611 0.036665453594658885 0.96847552398268411 0.24639562487829056 0.072361669300201478 -0.2484871639261669 0.96592852643454863
0.7526440675664261 -0.0012767262824115145 1e-10 1 0.5 0.5

Source Doc:
// <Tvec; 3 values> <Rotation matrix in row-major format; 9 values>
// <focal_length> <k1> <k2> 1.0 <principal point X> <principal point Y>
// Note that focal length is relative to the image max(width, height),
// and principal points x and y are relative to width and height respectively.

=====

Note: we want this in dataset folder:
colorIntrinsics.txt
depthIntrinsics.txt
frame-000000.color.png
frame-000000.depth.png
frame-000000.pose.txt
frame-000001.color.png
frame-000001.depth.png
frame-000001.pose.txt
...
"""

def colmap_cam_to_intrinsic3d_cam_pose_txt(colmap_cam_file_path):
    with open(colmap_cam_file_path, "r") as f:
        lines = f.readlines()
        nums = lines[0].strip().split(" ")
        t = [0] + nums[:3] 
        r1 = [0] + nums[3:6]
        r2 = [0] + nums[6:9]
        r3 = [0] + nums[9:]
    with open(colmap_cam_file_path.replace(".cam", ".pose.txt"), 'w') as f:
        f.write(f"""
{r1[1]} {r1[2]} {r1[3]} {t[1]}
{r2[1]} {r2[2]} {r2[3]} {t[2]}
{r3[1]} {r3[2]} {r3[3]} {t[3]}
""")


if __name__ == "__main__":
    import sys
    colmap_cam_to_intrinsic3d_cam_pose_txt(sys.argv[1])