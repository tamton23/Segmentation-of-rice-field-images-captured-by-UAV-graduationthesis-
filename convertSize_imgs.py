import cv2
import glob
import os
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
path = ''
file_path = 'Data_set/'
for filename in glob.glob(os.path.join(file_path, '*.JPG')):
    path = filename[9:]
    img = cv2.imread(filename)
    # reduce x8 size img
    h, w, c = img.shape
    imgScale = cv2.resize(img, (int(w/8), int(h/8)), interpolation = cv2.INTER_LINEAR)
    print('scale image shape: {}'.format(imgScale.shape))
    plt.subplot(121),plt.imshow(imgScale),plt.title('Origin Image')
    plt.subplot(122),plt.imshow(imgScale),plt.title('Scale Image')
    high, weight, ca = imgScale.shape
    print("({},{})".format(high, weight))
    cv2.imwrite("Data_set_resize/" + path, imgScale)
