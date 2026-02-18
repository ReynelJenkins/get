import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
def voltage_to_number(voltage):
    if not(0.0<=voltage<=3.3):
        print(f"Нпряжение выходит за динамический диапазон ЦАП(0.0-3.3 В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage/3.17*255)

def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]

dac_bits = dac_bits[::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)
led_pin=26
GPIO.output(led_pin, GPIO.OUT)
time.sleep(10)
GPIO.output(led_pin, 0)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах:"))
            number = voltage_to_number(voltage)
            print(number)
            GPIO.output(dac_bits, number_to_dac(number))
            
        except ValueError:
            print("Вы ввели не число, попробуйте еще раз\n")
            
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()