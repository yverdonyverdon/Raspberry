from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)
gpio_pin2 = Pin(19, Pin.IN)
gpio_pin3 = Pin(18, Pin.IN)

button_state = gpio_pin2.value()
light_on = False





while True:
    new_button_state = gpio_pin2.value()
    if new_button_state != button_state:
        if new_button_state == 1:
            light_on = not light_on
            gpio_pin.value(light_on)
        button_state = new_button_state
        time.sleep(0.2)
