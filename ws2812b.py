import array, time
from machine import Pin
import rp2

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()
    
class ws2812b:
    def __init__(self, num_leds, state_machine, pin):
        self.pixels = array.array("I", [0 for _ in range(num_leds)])
        self.sm = rp2.StateMachine(state_machine, ws2812, freq=8000000, sideset_base=Pin(pin))
        self.sm.active(1)
        self.num_leds = num_leds

    def set_pixel(self, pixel_num, red, green, blue):
        self.pixels[pixel_num] = blue | red << 8 | green << 16
        
    def show(self):
        for i in range(self.num_leds):
            self.sm.put(self.pixels[i],8)
            
    def fill(self, red, green, blue):
        for i in range(self.num_leds):
            self.set_pixel(i, red, green, blue)
        
        