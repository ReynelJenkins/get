import RPi.GPIO as GPIO
class R2R_DAC:
    def __init__(self, GPIO_bits, dynamic_range, verbose = False):
        self.GPIO_bits = GPIO_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO_bits, GPIO.OUT, initial = 0)


    def deinit(self):
        GPIO.output(self.GPIO_bits, 0)
        GPIO.cleanup()
    
    def DecToBin(self, value):
        return [int(i) for i in bin(value)[2:].zfill(8)]

    def set_number(self, number):
        for i in range(8):
            GPIO.output(self.GPIO_bits[i], self.DecToBin(number)[i])

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            self.set_number(0)
            return
        self.set_number(int(voltage / self.dynamic_range * 255))

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

