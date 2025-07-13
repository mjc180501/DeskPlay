from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI


COLORS = [
    color565(255, 0, 0),
    color565(0, 255, 0),
    color565(0, 0, 255),
    color565(255, 255, 0),
    color565(255, 0, 255),
    color565(0, 255, 255),
    color565(255, 128, 0),
    color565(128, 0, 255),
    color565(255, 255, 255),
]

def test():
    print("Starting colorful pattern demo")

    spi = SPI(0,
              baudrate=10000000,
              polarity=1,
              phase=1,
              bits=8,
              firstbit=SPI.MSB,
              sck=Pin(18),
              mosi=Pin(19),
              miso=Pin(16))

    display = Display(spi, dc=Pin(15), cs=Pin(17), rst=Pin(14))
    display.clear()

    step = 20
    for x in range(0, display.width, step):
        for y in range(0, display.height, step):
            color = COLORS[(x + y) // step % len(COLORS)]
            display.fill_rectangle(x, y, step - 2, step - 2, color)

test()
