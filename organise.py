import os
import shutil

from_dir = 'C:/Users/charl/Downloads/C102_assets-main'
to_dir = 'C:/Users/charl/Downloads/AllenImages'


list_of_files = os.listdir(from_dir)

for file in list_of_files:
    root,ext=os.path.splitext(file)

    if ext == '':
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + file  #C:/Users/charl/Downloads/C102_assets-main/badminton
        path2 = to_dir + '/' + "Image_Files" #C:/Users/charl/Downloads/AllenImage/Image_Files
        path3 = to_dir + '/' + "Image_Files" + '/' + file  #C:/Users/charl/Downloads/AllenImage/Image_Files/badminton
    
    if os.path.exists(path2):
        print("Moving "+ file + '....')
        shutil.move(path1,path3)
    
    else:
        os.makedirs(path2)
        print("Moving "+ file + '....')
        shutil.move(path1,path3)
