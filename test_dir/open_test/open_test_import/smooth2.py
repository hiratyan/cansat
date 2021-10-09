#!/usr/bin/python3

import cv2
import sys

def smooth(i):
    img2 = cv2.imread(i, cv2.IMREAD_COLOR )
    blur_img2 = cv2.blur(img2, (30,30) )
    cv2.imshow('Original image', img2) # 画像表示
    cv2.imshow('Blurred image', blur_img2) # 画像表示
    cv2.waitKey(0) # キー入力を待つ
    cv2.destroyAllWindows() # 画面表示を消去

