# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:42:26 2021

Author: Vaishak

Description :
Allows user to select ROI on an image and displays the select ROI in a new image windowss
"""

# Import modules
from cv2 import cv2

def select_roi(input_image) -> int:
    '''
    Description : Allows user to select the ROI on input image and give the coordinates points

    Arguments : InpImage->OpenCV Mat  = Input Image

    Returns : roiCoords -> tuple = Tuple of x, y, width and height
    '''

    text = 'SelectROI-PressEnterAfterSelection'
    x_cordinate, y_cordinate, width, height = cv2.selectROI(text, input_image)

    return x_cordinate, y_cordinate, width, height


def destory_windows():
    '''
    Description : destroys all image windows based on a user input
    '''
    key = cv2.waitKey(0)
    if key == ord('q'):     ##Press 'q' to close all figure windows
        cv2.destroyAllWindows()

if __name__ == '__main__':

    # Read Image
    INPUT_IMAGE = cv2.imread('Chrysanthemum.jpg')

    # Process
    X, Y, WIDTH, HEIGHT = select_roi(INPUT_IMAGE)

    #Crop Image
    CROPPED_IMAGE = INPUT_IMAGE[Y:Y+HEIGHT, X:X+WIDTH]

    # Display Cropped Image
    cv2.imshow('SelectImageROI-PressEnterAfterSelection', CROPPED_IMAGE)

    # Destory windows
    destory_windows()
