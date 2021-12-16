import RPi.GPIO as GPIO
import time

Ain1 = 26
Ain2 = 22
Bin1 = 27
Bin2 = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(Ain1, GPIO.OUT)
GPIO.setup(Ain2, GPIO.OUT)
GPIO.setup(Bin1, GPIO.OUT)
GPIO.setup(Bin2, GPIO.OUT)

GPIO.output(Bin1, True)
time.sleep(1)
GPIO.output(Bin1, False)
time.sleep(1)
GPIO.output(Bin2, True)
time.sleep(1)
GPIO.output(Bin2, False)
time.sleep(1)

GPIO.cleanup()
