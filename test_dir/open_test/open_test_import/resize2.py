#!/usr/bin/python3

import cv2
import sys

def resize():
    img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )
    img_height = img.shape[0]
    img_width = img.shape[1]
    small_img_height = int( img_height / 2 )
    small_img_width = int( img_width / 2 )
    return cv2.resize( img, (small_img_height, small_img_width ) )

def test():
    img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )
    img_height = img.shape[0]
    img_width = img.shape[1]
    small_img_height = int( img_height / 2 )
    small_img_width = int( img_width / 2 )
    small_img = cv2.resize( img, (small_img_height, small_img_width ) )
    cv2.imshow('Original image', img) 
    cv2.imshow('Small image', small_img) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 


if __name__ == "__main__":
    test()