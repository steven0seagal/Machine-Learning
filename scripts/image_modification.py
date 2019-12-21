
import sys
import os
import cv2
import numpy as np

data_path = os.getcwd()
os.chdir('../')
data_path = os.getcwd()
# Load and display an image -- 'forest.jpg'
input_file = data_path + '\\data\\' + 'forest.jpg'

img = cv2.imread(input_file)
cv2.imshow('Orginal', img)

# Cropping an image (acting as it is matrix of raw data )
h, w = img.shape[:2]
start_row, end_row = int(0.21*h), int(0.73*h)
start_col, end_col= int(0.37*w), int(0.92*w)
img_cropped = img[start_row:end_row, start_col:end_col]
cv2.imshow('Cropped', img_cropped)

# Resizing an image (factor is important)
scaling_factor = 1.4
img_scaled = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor,
        interpolation=cv2.INTER_LINEAR)
cv2.imshow('Uniform resizing', img_scaled)
img_scaled = cv2.resize(img, (250, 400), interpolation=cv2.INTER_AREA)
cv2.imshow('Skewed resizing', img_scaled)

# Save an image
output_file = input_file[:-4] + '_cropped.jpg'
cv2.imwrite(output_file, img_cropped)


cv2.waitKey()
