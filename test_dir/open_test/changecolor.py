#!/usr/bin/python3
# OpenCV2 をインポートして利用できるようにする
import cv2
import sys # 引数処理のため sys ライブラリをインポート

# 画像の読み込み
img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )

# 入力画像をコピーして img2 を生成
img2 = img.copy()
for x in range( img2.shape[0] ):
    for y in range( img2.shape[1] ):
        b_val = img2[x,y,0] # Blue の画素値
        g_val = img2[x,y,1] # Green の画素値
        r_val = img2[x,y,2] # Red の画素値

        if ( b_val < 70 ) and ( g_val < 70 ) and ( r_val > 100 ):
            pass
        else:
            val = int(0.299*r_val + 0.587*g_val + 0.114*b_val)
            img2[x,y,0] = val
            img2[x,y,1] = val
            img2[x,y,2] = val
            
cv2.imshow('Original image', img) # 画像表示
cv2.imshow('Modified image', img2) # 画像表示
cv2.waitKey(0) # キー入力を待つ
cv2.destroyAllWindows() # 画面表示を消去