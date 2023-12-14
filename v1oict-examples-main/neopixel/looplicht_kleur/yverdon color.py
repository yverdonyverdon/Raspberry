import time
import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

while True:
    # Rood
    for i in range(8):
        np[i] = (255, 0, 0)
        np.write()
        time.sleep(1)

    # Groen
    for i in range(8):
        np[i] = (0, 255, 0)
        np.write()
        time.sleep(1)

    # Blauw
    for i in range(8):
        np[i] = (0, 0, 255)
        np.write()
        time.sleep(1)
