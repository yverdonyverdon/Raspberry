from machine import Pin
import time

led_pins = [
    Pin(0, Pin.OUT),
    Pin(1, Pin.OUT),
    Pin(2, Pin.OUT),
    Pin(3, Pin.OUT),
    Pin(4, Pin.OUT)
]

def leds(value, delay):
    for led in led_pins:
        if value % 2 == 1:
            led.value(1)
        else:
            led.value(0)
        value = value // 2
    time.sleep(delay)

delay = 0.2

while True:
    for i in range(16):  # Loop van 0 tot 15
        leds(i, delay)

    for i in range(14, 0, -1):  # Loop van 14 tot 1 in omgekeerde volgorde
        leds(i, delay)

