#!/usr/bin/python3

#平滑化の種類（blurかGaussianBlur）とパラメータを選択して保存する．
#python3 blur_or_gauss.py input_img blur(gauss) size1 size2 (sigmaX)
#sys.argv[1] = input_img
#sys.argv[2] = blur(gauss)
#sys.argv[3] = size1
#sys.argv[4] = size2
#sys.argv[5] = sigmaX

import cv2
import sys

img = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)

if sys.argv[2] == 'blur':  
    blur_img = cv2.blur(img, (int(sys.argv[3]), int(sys.argv[4])))
    cv2.imshow('Original image', img)
    cv2.imshow('Blurred image',blur_img)
    cv2.imwrite('blurred.jpg',blur_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows

#gaussのときは大きな数字を選択できない
elif sys.argv[2] == 'gauss':
    gauss_img = cv2.GaussianBlur(img, (int(sys.argv[3]), int(sys.argv[4])), int(sys.argv[5]))
    cv2.imshow('Original image', img)
    cv2.imshow('Gauss image', gauss_img)
    cv2.imwrite('gauss.jpg', gauss_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows

else: 
    print('not')