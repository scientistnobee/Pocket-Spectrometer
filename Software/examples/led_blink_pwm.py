#
# Example of blinking LED with different intensity
#

import sys
from time import sleep_ms
from machine import I2C, SoftI2C, Pin

# i2c = SoftI2C(scl=Pin(27), sda=Pin(33))
i2c = I2C(0)
addrlist = " ".join(["0x{:02X}".format(x) for x in i2c.scan()])
print("Detected devices at I2C-addresses:", addrlist)

from as7341 import *

sensor = AS7341(i2c)
if not sensor.isconnected():
    print("Failed to contact AS7341, terminating")
    sys.exit(1)

def blink_led(n, freq, curr):
    print("Blink LED {:d} times at freq {:d} Hz with {:d} mA".format(n, freq, curr))
    for _ in range(n):
        sensor.set_led_current(curr)    # LED on with <curr> mA
        sleep_ms(500 // freq)           # half period
        sensor.set_led_current(0)       # LED effectively off
        sleep_ms(500 // freq)           # half period

try:
    while True:
        blink_led(2, 1, 4)              # blink 2 times at 1 Hz with 4 mA
        blink_led(4, 2, 20)             # blink 4 times at 2 Hz with 20 mA

except KeyboardInterrupt:
    print("Interrupted from keyboard")

sensor.set_led_current(0)               # LED off
sensor.disable()

#
