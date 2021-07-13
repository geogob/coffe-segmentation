#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:16:11 2021

@author: george
"""

import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = Image.open('/home/george/dataset-multiespectrais/IMG_200911_190650_0004_RGB_modificado.tif')
img = np.array(img)
cv.imshow("test", img)