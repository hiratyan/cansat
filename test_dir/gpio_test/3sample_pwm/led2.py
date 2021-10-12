import RPi.GPIO as GPIO # RPi をインポート
import time

# BOARD 番号で GPIO を設定
GPIO.setmode(GPIO.BCM)

# 21 番ピンを出力 (GPIO.OUT) に設定
GPIO.setup(21, GPIO.OUT)

# 21 番ピンを pwm として 1000Hz で動作させる
pwm = GPIO.PWM(21, 1000)

# デューティ比 20 でスタート
pwm.start(20)
time.sleep(1) # 1 秒待つ

# デューティ比を 70 に変更
pwm.ChangeDutyCycle(70)
time.sleep(1) # 1 秒待つ

# PWM 出力を停止する
pwm.stop()

# GPIO の終了処理
GPIO.cleanup()