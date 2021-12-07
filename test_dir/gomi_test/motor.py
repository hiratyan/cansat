import RPi.GPIO as GPIO
import time

in1_pin = 27
in2_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)

for i in range(5):
    GPIO.output(in1_pin, True)
    time.sleep(3)
    GPIO.output(in1_pin, False)
    time.sleep(3)
GPIO.cleanup()
