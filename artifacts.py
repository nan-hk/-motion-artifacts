import os
import numpy as np
import nibabel as nib

data_path = "/nhk/Spring2022/-motion-artifacts/dataset/GT/"
test_dataset = os.path.join(data_path, "GT_0.nii")

img = nib.load(test_dataset)
print(img.shape)
