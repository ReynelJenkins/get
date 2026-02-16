import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17,27,23,22,24]
GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds,0)
up_p = 9
down_p = 10
GPIO.setup(up_p,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(down_p,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
num = 0
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)
delay = 0.2

try:
    while True:
        if GPIO.input(up):
            num = num+1
            if num > 255:
                num = 255
            print(num,dec2bin(num))
            time.sleep(delay)
        
        if GPIO.input(down):
            num = num-1
        if num < 0:
            num = 0
        print(num,dec2bin(num))
        time.sleep(delay)
    GPIO.output(leds,dec2bin(num))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print('klkaa')
