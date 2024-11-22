#
# Example of use of GPIO pin as input
#

from time import sleep_ms
from machine import I2C, SoftI2C, Pin

# i2c = SoftI2C(scl=Pin(27), sda=Pin(33))
i2c = I2C(0)
addrlist = " ".join(["0x{:02X}".format(x) for x in i2c.scan()])
print("Detected devices at I2C-addresses:", addrlist)

from as7341 import *
sensor = AS7341(i2c)

sensor.set_gpio_input(True)     # enable input mode

try:
    while True:
        print("GPIO is ", "high" if sensor.get_gpio_value() else "low")
        sleep_ms(3000)

except KeyboardInterrupt:
    print("Interrupted from keyboard")

sensor.disable()

#
