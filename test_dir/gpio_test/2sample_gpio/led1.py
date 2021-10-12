import RPi.GPIO as GPIO # RPi をインポート
import time

# BCM 番号で GPIO を設定
GPIO.setmode(GPIO.BCM)

# 21 番ピンを出力 (GPIO.OUT) に設定
GPIO.setup(21, GPIO.OUT)

# 21 番ピンを ON(True) にする
GPIO.output(21, True)

# 1 秒待つ
time.sleep(1.0)

# 21 番ピンを OFF(False) にする
GPIO.output(21, False)

# GPIO の終了処理
GPIO.cleanup()