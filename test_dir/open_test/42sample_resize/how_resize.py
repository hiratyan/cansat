#!/usr/bin/python3

#引数でサイズと保管方法を指定できるようにして保存する．
#python3 how_resize.py input_img type size1 size2
#sys.argv[1] = input_img
#sys.argv[2] = type
#sys.argv[3] = size1
#sys.argv[4] = size2
#type = near, line, area, cube, lanc

import cv2
import sys

img = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)

if sys.argv[2] == "near":
    near_img = cv2.resize(img, (int(sys.argv[3]), int(sys.argv[4])), interpolation=cv2.INTER_NEAREST)
    cv2.imshow('Original image', img)
    cv2.imshow('NEAREST image',near_img)
    cv2.imwrite('NEAREST.jpg',near_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows

elif sys.argv[2] == "line":
    line_img = cv2.resize(img, (int(sys.argv[3]), int(sys.argv[4])), interpolation=cv2.INTER_LINEAR)
    cv2.imshow('Original image', img)
    cv2.imshow('LINEAR image',line_img)
    cv2.imwrite('LINEAR.jpg',line_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows

elif sys.argv[2] == "area":
    area_img = cv2.resize(img, (int(sys.argv[3]), int(sys.argv[4])), interpolation=cv2.INTER_AREA)
    cv2.imshow('Original image', img)
    cv2.imshow('AREA image',area_img)
    cv2.imwrite('AREA.jpg',area_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows

elif sys.argv[2] == "cube":
    cube_img = cv2.resize(img, (int(sys.argv[3]), int(sys.argv[4])), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Original image', img)
    cv2.imshow('CUBIC image',cube_img)
    cv2.imwrite('CUBIC.jpg',cube_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows

elif sys.argv[2] == "lanc":
    lanc_img = cv2.resize(img, (int(sys.argv[3]), int(sys.argv[4])), interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow('Original image', img)
    cv2.imshow('LANCZOS4 image',lanc_img)
    cv2.imwrite('LANCZOS4.jpg',lanc_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows

else:
    print("not")