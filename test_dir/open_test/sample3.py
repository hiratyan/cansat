#!/usr/bin/python3
# OpenCV2 をインポートして利用できるようにする
import cv2
# カメラの準備
cap = cv2.VideoCapture(0)
# 無限にループする
while True:
# カメラから画像を読み取り,img に格納する
ret, img = cap.read()
# 画像を表示する
cv2.imshow(’image’, img)
# キー入力を待つ
c = cv2.waitKey(1000)
# ESC キーが押されたら終了する
if c == 27:
break;
# デバイスを解放する
cap.release()
# 画面表示を消去
cv2.destroyAllWindows()