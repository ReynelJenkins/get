import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
l = 26 
sensor = 6
GPIO.setup(l,GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)
while True:
    state = GPIO.input(sensor)
    GPIO.output(l,not state)
    time.sleep(0.05)

