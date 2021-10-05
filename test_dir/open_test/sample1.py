#!/usr/bin/python3
# OpenCV2 をインポートして利用できるようにする
import cv2
import sys # 引数処理のため sys ライブラリをインポート
# 画像の読み込み
img = cv2.imread( sys.argv[1], cv2.IMREAD_COLOR )
# 画像を表示する
cv2.imshow(’image’, img)
# キー入力を待つ.引数 0 は入力を待ち続ける.10 なら 10 ミリ秒待つ.
cv2.waitKey(0)
# 画面表示を消去
cv2.destroyAllWindows()