#!/usr/bin/python3

# OpenCV2 をインポートして利用できるようにする
import cv2
import sys # 引数処理のため sys ライブラリをインポート

# 画像の読み込み
img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )

# 平滑化
blur_img = cv2.blur(img, (30,30) )
cv2.imshow('Original image', img) # 画像表示
cv2.imshow('Blurred image', blur_img) # 画像表示
cv2.waitKey(0) # キー入力を待つ
cv2.destroyAllWindows() # 画面表示を消去