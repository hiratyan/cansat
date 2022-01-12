import RPi.GPIO as GPIO
import sys
import time
import cv2

cap = cv2.VideoCapture(0)
duty = 80

#GPIO初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

r1 = GPIO.PWM(26, 50) #50Hz
r2 = GPIO.PWM(22, 50) #50Hz
l1 = GPIO.PWM(27, 50) #50Hz
l2 = GPIO.PWM(17, 50) #50Hz
            
r1.start(0)
r2.start(0)
l1.start(0)
l2.start(0)

try:
    while True:
        # カメラから画像を読み取り,img に格納する
        ret, img = cap.read()
# 画像を表示する
        cv2.imshow('image', img)
# キー入力を待つ
        c = cv2.waitKey(1000)
# ESC キーが押されたら終了する
        if c == 27:
            break;
# デバイスを解放する
        cap.release()
# 画面表示を消去
        cv2.destroyAllWindows()

        #「g」キーが押されたら前進
        c = sys.stdin.read(1)
        if c == 'e':
            r1.ChangeDutyCycle(duty)
            r2.ChangeDutyCycle(0)
            l1.ChangeDutyCycle(duty)
            l2.ChangeDutyCycle(0) 

        #「b」キーが押されたら後退
        if c == 'd':
            r1.ChangeDutyCycle(0)
            r2.ChangeDutyCycle(duty)
            l1.ChangeDutyCycle(0)
            l2.ChangeDutyCycle(duty)

        #「q」キーが押されたら止まる
        if c == 'q':
            r1.ChangeDutyCycle(0)
            r2.ChangeDutyCycle(0)
            l1.ChangeDutyCycle(0)
            l2.ChangeDutyCycle(0)

        #「r」キーが押されたら右へ曲がる
        if c == 'r':
            r1.ChangeDutyCycle(30)
            r2.ChangeDutyCycle(0)
            l1.ChangeDutyCycle(0)
            l2.ChangeDutyCycle(0)

        #「l」キーが押されたら右へ曲がる
        if c == 'l':
            r1.ChangeDutyCycle(0)
            r2.ChangeDutyCycle(0)
            l1.ChangeDutyCycle(30)
            l2.ChangeDutyCycle(0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
