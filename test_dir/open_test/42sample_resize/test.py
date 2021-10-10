#!/usr/bin/python3

import cv2
import sys

img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )

small_img = cv2.resize( img, (30, 30), interpolation=cv2.INTER_LINEAR )
cv2.imshow('Original image', img)
cv2.imshow('Small image', small_img)
cv2.waitKey(0)
cv2.destroyAllWindows()