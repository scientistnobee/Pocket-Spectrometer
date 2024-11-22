#
# Example of use of GPIO pin as ouput to control a LED
#

from time import sleep_ms
from machine import I2C, SoftI2C, Pin

# i2c = SoftI2C(scl=Pin(27), sda=Pin(33))
i2c = I2C(0)
addrlist = " ".join(["0x{:02X}".format(x) for x in i2c.scan()])
print("Detected devices at I2C-addresses:", addrlist)

from as7341 import *
sensor = AS7341(i2c)

sensor.set_gpio_output(True)       # enable output mode, inverted
print("Starting with LED OFF for 3 seconds")
sleep_ms(3000)

try:
    while True:
        sensor.set_gpio_inverted(False)
        print("LED ON 1 second")
        sleep_ms(1000)
        sensor.set_gpio_inverted()
        print("LED off 0.5 seconds")
        sleep_ms(500)
        

except KeyboardInterrupt:
    print("Interrupted from keyboard")

sensor.disable()

#
