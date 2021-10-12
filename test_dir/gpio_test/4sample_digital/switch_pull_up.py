import RPi.GPIO as GPIO # RPi をインポート
import time

# BOARD 番号で GPIO を設定
GPIO.setmode(GPIO.BCM)

# 21 番ピンを入力 (GPIO.IN) に設定
# プルダウンに設定 ( 開放状態のとき 0)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# ピン 21 の状態を表示
try:
    while True:
        print("Status: ", GPIO.input(21))
        time.sleep(1.0)
except KeyboardInterrupt as err:
    pass

# GPIO の終了処理
GPIO.cleanup()