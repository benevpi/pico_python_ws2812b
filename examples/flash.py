import time
from ws2812b import ws2812b

num_leds = 30
pixels = ws2812b(num_leds, 0,0)

while True:
    for i in range(30):
        for j in range(30):
            pixels.set_pixel(j,abs(i+j)%10,abs(i-(j+3))%10,abs(i-(j+6))%10)          
        pixels.show()
        time.sleep(0.05)


