#!/usr/bin/python3
import cv2
# しきい値
THRESHOLD=5000000
cap = cv2.VideoCapture(0)
ret, refimg = cap.read()
# 画像をグレースケールに変換し,表示する.
gray_refimg = cv2.cvtColor(refimg, cv2.COLOR_BGR2GRAY)
cv2.imshow('Reference Image', gray_refimg)
# 無限にループする
while True:
# カメラから画像を読み取り,グレースケールに変換する
    ret, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 差分画像を求め,表示する
    diff_img = cv2.absdiff( gray_refimg, gray_img )
    cv2.imshow('Diff Image', diff_img)
# 差分画像の画素値の総和を求め,表示する
    sumvalue = cv2.sumElems( diff_img )
    print('sumvalue = ' + str(sumvalue[0]) )
# 差分画像の画素値の総和がしきい値以上なら表示画像を更新する
    if sumvalue[0] >= THRESHOLD:
        gray_refimg = gray_img
        cv2.imshow('Reference Image', gray_refimg)

    c = cv2.waitKey(100)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()