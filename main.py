import os
import shutil

from_dir = "DIR1"
to_dir = "DIR2"

list_of_files = os.listdir(from_dir)

for i in list_of_files:
    name,extension = os.path.splitext(i)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/image_files"
        path3 = to_dir + "/image_files/" + i
        if os.path.exists(path2):
            print("Moving file from " + path1 + " to " + path3)
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving file from " + path1 + " to " + path3)
            shutil.move(path1, path3)
