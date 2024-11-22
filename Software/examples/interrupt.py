#
# Example of interrupt and thresholds handling of the AS7341
#

import sys
from machine import I2C, SoftI2C, Pin
from time import sleep_ms

# i2c = SoftI2C(scl=Pin(27), sda=Pin(33))
i2c = I2C(0)#
print("Detected devices at I2C-addresses:", i2c.scan())

from as7341 import *

sensor = AS7341(i2c)
if not sensor.isconnected():
    print("Failed to contact AS7341, terminating")
    sys.exit(1)

sensor.set_measure_mode(AS7341_MODE_SPM)
sensor.set_spectral_interrupt(1)
sensor.set_atime(29)
sensor.set_astep(599)
sensor.set_again(4)
sensor.set_thresholds(200, 900)
sensor.set_interrupt_persistence(0)
sensor.set_spectral_threshold_channel(4)    # clear channel

try:

    while True:
        sensor.clear_interrupt()
        sensor.start_measure("F1F4CN")      # channel mapping
        _,_,_,_,clear,_ = sensor.get_spectral_data()
        print("Clear: {:d}".format(clear))
        if sensor.check_interrupt():
            print("Interrupt detected!")
        else:
            print("no interrupt ....")
        sleep_ms(3000)

except KeyboardInterrupt:
    print("Interrupted from keyboard")

sensor.disable()

#
