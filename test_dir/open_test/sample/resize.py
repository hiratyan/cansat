#!/usr/bin/python3
# OpenCV2 をインポートして利用できるようにする
import cv2
import sys # 引数処理のため sys ライブラリをインポート

# 画像の読み込み
img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )
# 画像のサイズを取得
img_height = img.shape[0]
img_width = img.shape[1]
# 新しい画像のサイズを設定
small_img_height = int( img_height / 2 )
small_img_width = int( img_width / 2 )
# 画像のサイズを縦横 1/2 にする
small_img = cv2.resize( img, (small_img_height, small_img_width ) )
cv2.imshow('Original image', img) # 画像表示
cv2.imshow('Small image', small_img) # 画像表示
cv2.waitKey(0) # キー入力を待つ
cv2.destroyAllWindows() # 画面表示を消去