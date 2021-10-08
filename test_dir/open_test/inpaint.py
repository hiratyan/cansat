#!/usr/bin/python3
# OpenCV2 をインポートして利用できるようにする
import cv2
import sys # 引数処理のため sys ライブラリをインポート

# 画像の読み込み
img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )

# マスク画像の読み込み
mask_img = cv2.imread( sys.argv[2], cv2.IMREAD_GRAYSCALE )

# 入力画像をコピーして damaged_img を生成
damaged_img = img.copy()
# 入力画像とマスク画像をから欠損画像を生成
damaged_img[:,:,0] = img[:,:,0] & (255- mask_img)
damaged_img[:,:,1] = img[:,:,1] & (255- mask_img)
damaged_img[:,:,2] = img[:,:,2] & (255- mask_img)
cv2.imshow('Damaged image', damaged_img) # 画像表示
# 画像修復
inpaint_img = cv2.inpaint(damaged_img, mask_img, 3, cv2.INPAINT_NS)
cv2.imshow('Inpaint image', inpaint_img) # 画像表示
cv2.waitKey(0) # キー入力を待つ
cv2.destroyAllWindows() # 画面表示を消去