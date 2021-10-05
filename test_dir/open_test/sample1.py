#!/usr/bin/python3

# OpenCV2 をインポートして利用できるようにする
import cv2

# 引数処理のため sys ライブラリをインポート
import sys

# 画像の読み込み
# sys.argsについて
# https://qiita.com/orange_u/items/3f0fb6044fd5ee2c3a37
# sys.argv[1]は例でいうと pic/Indoors/room1.jpg
# cv2.imread,cv2.IMREAD_COLOR,cv2.waitKeyについて
# https://weblabo.oscasierra.net/python/opencv-image.html
img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )


# 画像を表示する
# 第一引数はウインドウ名
cv2.imshow(’image’, img)

# キー入力を待つ.引数 0 は入力を待ち続ける.10 なら 10 ミリ秒待つ.
cv2.waitKey(0)

# 画面表示を消去
cv2.destroyAllWindows()