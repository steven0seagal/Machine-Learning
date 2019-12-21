import sys

import os
import cv2
import numpy as np

data_path = os.getcwd()
os.chdir('../')
data_path = os.getcwd()
# Load and display an image -- 'forest.jpg'
input_file = data_path + '\\data\\' + 'sunrise.jpg'
# Load the input image -- 'chair.jpg'
# Convert it to grayscale
img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
h, w = img.shape

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
canny = cv2.Canny(img, 50, 240)

cv2.imshow('Original', img)
cv2.imshow('Sobel horizontal', sobel_horizontal)
cv2.imshow('Sobel vertical', sobel_vertical)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Canny', canny)

cv2.waitKey()

