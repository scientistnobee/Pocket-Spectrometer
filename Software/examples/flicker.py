#
# Example of flicker detection
#

import sys
from machine import I2C, SoftI2C, Pin
from time import sleep_ms

# i2c = SoftI2C(scl=Pin(27), sda=Pin(33))
i2c = I2C(0)
addrlist = " ".join(["0x{:02X}".format(x) for x in i2c.scan()])
print("Detected devices at I2C-addresses:", addrlist)

from as7341 import *

sensor = AS7341(i2c)
if not sensor.isconnected():
    print("Failed to contact AS7341, terminating")
    sys.exit(1)

sensor.set_measure_mode(AS7341_MODE_SPM)  # (SPM mode)
sensor.set_atime(29)                 # 30 ASTEPS
sensor.set_astep(599)                # ASTEP = 1.67 ms
sensor.set_again(4)                  # factor 8 (for with pretty much light)

try:
    while True:
        flicker_freq = sensor.get_flicker_frequency()
        if flicker_freq == 0:
            print("No flicker detected!")
        else:
            print("Flicker frequency: {:d} Hz".format(flicker_freq))
        sleep_ms(3000)

except KeyboardInterrupt:
    print("Interrupted from keyboard")

sensor.disable()

#
