from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from machine import Pin
import machine

"""
From the 1602A LCD Datasheet. The I2C 1602 LCD module is a 2 line by 16 character display interfaced to an I2C daughter board.
Specifications: 2 lines by 16 characters
I2C Address Range: 0x20 to 0x27 (Default=0x27, addressable) 
Operating Voltage: 5 Vdc 
Contrast: Adjustable by potentiometer on I2C interface
Size: 80mm x 36mm x 20 mm
Viewable area: 66mm x 16mm 

Drivers provided by https://www.circuitschools.com/
Note: Adjust the potentiometer when you do not see any characters on the display 
"""

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

adcpin = 4
sensor = machine.ADC(adcpin)


def temperatuur():
    adc_value = sensor.read_u16()
    volt = (3.3 / 65535) * adc_value
    temperature = 27 - (volt - 0.706) / 0.001721
    temperature = (round(temperature, 1))
    return temperature



while True:
    print(I2C_ADDR, "| Hex:", hex(I2C_ADDR))
    lcd.move_to(0, 0)
    lcd.putstr("Temperatuur is" + "\n")
    lcd.move_to(0, 1)
    lcd.putstr(f"{temperatuur()}")
