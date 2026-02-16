import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
def dec2bin(value):
        return[int(element) for element in bin(value)[2:].zfill(8)]
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17,27,23,22,24]
up_p = 9
down_p = 10
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(up_p,GPIO.IN)
GPIO.setup(down_p,GPIO.IN)
GPIO.output(leds,0)
num = 0
sleep_time = 0.2
while True:
    if GPIO.input(up_p):
        num = min((num+1),255)
        time.sleep(sleep_time)
        print(num,dec2bin(num))
    if GPIO.input(down_p):
        num = max((num-1),0)
        time.sleep(sleep_time)
        print(num,dec2bin(num))
    GPIO.output(leds,dec2bin(num))
