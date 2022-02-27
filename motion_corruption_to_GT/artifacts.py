import os
import numpy as np
import nibabel as nib
from motion_corruption import load_image, manipulate_kspace_columns, image_reconstruction, write_image, generate_motion_trajectory

input_dir = "/nhk/Spring2022/-motion-artifacts/dataset/GT/"

for root,dirnames,filenames in os.walk(input_dir):
        for image in sorted(filenames):
            filepath = os.path.join(root, image)
            if '.nii' in filepath: 
                image, array = load_image(filepath)
                imagesize = image.GetSize()
                print(filepath)
                print(imagesize)
                motion_table=generate_motion_trajectory(imagesize)
                np.save(root+'/motion_table',motion_table)
                corrupted_data = manipulate_kspace_columns(motion_table,filepath,imagesize)
                corrupted_image = image_reconstruction(corrupted_data)
                write_image(root,corrupted_image)