import machine
import time


num_leds = 30


sensor_temp = machine.ADC(4)
blah = machine.ADC(3) # comment or uncomment this line to trigger / untrigger


conversion_factor = 3.3 / 65535

min_temp = 0
max_temp = 30

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    time.sleep(0.5)
    