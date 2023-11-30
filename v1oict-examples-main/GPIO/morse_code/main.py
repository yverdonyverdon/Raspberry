from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):
    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


def morse(pin, dot_length, text):
    morse_code = {
        ' ': ' ',
        '-': '-',
        '.': '.',
        }

    for char in text:
        if char == '.':
            pulse(pin, dot_length, dot_length)
        elif char == '-':
            pulse(pin, 3*dot_length, dot_length)
        elif char == ' ':
            time.sleep(7*dot_length)


morse(gpio_pin, 0.2, ".--. -.-- - .... --- -.")
