"""
im_resize.py
Downsample the images.
In openCV, image f = (x, y) where x is the height, and y is the width
"""

import cv2

import os
path = '/home/d/caffe/data/skinimages/val/'
lst = os.listdir(path + 'Orig')
dim = (128, 128)

for i in range (len(lst)):

    print (path + str(lst[i]))
    im = cv2.imread(path +'Orig/' + str(lst[i]))
    cropped = im[200:(200+512), 200:(200+512)]
    cv2.imwrite(path + 'Cropped/'+ 'cropped_' + str(lst[i]), cropped)
    resized = cv2.resize(cropped, dim, interpolation = cv2.INTER_LINEAR)
    cv2.imwrite(path + 'Crop_Downsmpld/'+ 'crp_down' + str(lst[i]), resized)



"""

#path to the image(s)
path = '/home/d/caffe/data/skinimages/train/ISIC_0.jpg0000000.jpg'

for i in range():
    im = cv2.read(o)


"""
"""
#load the image
im = cv2.imread(path)
#cv2.imshow('orig', im)
#cv2.waitKey(0)

# New dimensions of the Image
dim = (512, 512)

# Cropping of the image
cropped = im[156:(156+512), 146: (146+512)]
cv2.imshow('crop', cropped)
cv2.waitKey(0)
"""
