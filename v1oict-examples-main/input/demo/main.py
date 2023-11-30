from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)
aan_pin = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)
uit_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if aan_pin.value():
        led_pin.value(1)
    elif uit_pin.value():
        led_pin.value(0)
    time.sleep(0.1)