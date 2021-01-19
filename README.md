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

A simple example is the following typed into the interpreter:

```
>>> import ws2812b
>>> pixels = ws2812b.ws2812b(10,0,0)
>>> pixels.show()
>>> pixels.set_pixel(5,10,0,0)
>>> pixels.show()
>>> pixels.set_pixel(5,0,10,0)
>>> pixels.show()
```

Pull requests are open if you'd like more features!
