#
# Example of sysns reading of
#

import sys
from time import sleep_ms
from machine import I2C, Pin

# i2c = SoftI2C(scl=Pin(27), sda=Pin(33))
i2c = I2C(0)
addrlist = " ".join(["0x{:02X}".format(x) for x in i2c.scan()])
print("Detected devices at I2C-addresses:", addrlist)

from as7341 import *

sensor = AS7341(i2c)
if not sensor.isconnected():
    print("Failed to contact AS7341, terminating")
    sys.exit(1)

sensor.set_measure_mode(AS7341_MODE_SYNS)   #
sensor.set_atime(29)                 # 30 ASTEPS
sensor.set_astep(599)                # 1.67 ms
sensor.set_again(4)                  # factor 8 (with pretty much light)

try:

    while True:

        print("Waiting for the GPIO signal...")
        sensor.start_measure("F2F7")
        while not sensor.measurement_completed():
            sleep_ms(100)
        f2,f3,f4,f5,f6,f7 = sensor.get_spectral_data()
        print("F2 (405-425nm): {:d}".format(f2))
        print("F3 (435-455nm): {:d}".format(f3))
        print("F4 (470-490nm): {:d}".format(f4))
        print("F5 (505-525nm): {:d}".format(f5))
        print('F6 (580-600nm): {:d}'.format(f6))
        print('F7 (620-640nm): {:d}'.format(f7))

        print("-----------------------")

except KeyboardInterrupt:
    print("Interrupted from keyboard")

sensor.disable()

#
