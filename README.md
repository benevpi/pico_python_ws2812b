# Retired
This library is now retired and won't be getting updates. There's an improved version here: https://github.com/blaz-r/pi_pico_neopixel This version extends the code here and includes support for RGBW LEDs as well as RGB leds with the R, G and B components in a different order.

I'll leave the code here for the foreseeable future, so feel free to use it, extend it or modify it as you see fit, but the above library is an improvement.


# pico_ws2812b
a library for using WS2812b leds (aka neopixels) with Raspberry Pi Pico

![neopixels in action](
https://github.com/benevpi/pico_python_ws2812b/blob/main/pico_ws2812b.jpg)


You'll first need to save the ws2812b.py file to your device (for example, open it in Thonny and go file > save as and select MicroPython device. Give it the same name). Once it's there, you can import it into your code. 

You create an object with the parameters number of LEDs, state machine ID and GPIO number in that order. so, to create a strip of 10 leds on state machine 0 and GPIO 0, you use:

```
pixels = ws2812b.ws2812b(10,0,0)
```

This object has two methods, show() which sends the data to the strip, and set_pixel which sets the colour values for a particular LED. The parameters are LED number, red, green, blue with the colours taking values between 0 and 255.

At the moment, this isn't working with the interpreter, so you have to run it from a file. Looks like it's running just too slow to keep up with the PIO buffer from the interpreter. The key methods are set_pixel(r,g,b), set_pixel_line(p1, p2, r, g, b) which sets a row of pixels from pixel p1 to pixel p2 (inclusive), and fill(r,g,b) which fills all the pixels with the colour r,g,b.

```
pixels.set_pixel(5,10,0,0)
pixels.set_pixel_line(5,7,0,10,0)
pixels.fill(20,5,0)
```

Pull requests are open if you'd like more features!
