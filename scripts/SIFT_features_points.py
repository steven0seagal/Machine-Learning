import sys
import os
import cv2
import numpy as np

# Load input image -- 'table.jpg'
data_path = os.getcwd()
os.chdir('../')
data_path = os.getcwd()
input_file = data_path + '\\data\\' + 'table.jpg'
img = cv2.imread(input_file)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
keypoints = sift.detect(img_gray, None)

img_sift = np.copy(img)
cv2.drawKeypoints(img, keypoints, img_sift, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Input image', img)
cv2.imshow('SIFT features', img_sift)
cv2.waitKey()
cv2