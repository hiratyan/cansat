#!/usr/bin/python3

import cv2
import sys

def resize():
    img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )
    small_img = cv2.resize( img, (int (img.shape[0]/2),  (int (img.shape[1]/2) )

def test():
    img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )
    small_img = cv2.resize( img, (int (img.shape[0]/2),  (int (img.shape[1]/2) )
    cv2.imshow('Original image', img) # 画像表示
    cv2.imshow('Small image', small_img) # 画像表示
    cv2.waitKey(0) # キー入力を待つ
    cv2.destroyAllWindows() # 画面表示を消去


if __name__ == "__main__":
    test()