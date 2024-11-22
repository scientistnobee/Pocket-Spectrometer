#
# Example of pin interrupts of the AS7341
#

import sys
from time import sleep_ms
from machine import I2C, SoftI2C, Pin

# i2c = SoftI2C(scl=Pin(27), sda=Pin(33))
i2c = I2C(0)
print("Detected devices at I2C-addresses:", i2c.scan())

from as7341 import *

sensor = AS7341(i2c)
if not sensor.isconnected():
    print("Failed to contact AS7341, terminating")
    sys.exit(1)

led = Pin(34, Pin.OUT)                       
def pinint_toggle(x):
    # toggle Pin
    print("pinint", str(x), x.value())
    if led.value():
        led.off()
    else:
        led.on()

print("Toggle LED on pin 34, with every interrupt on pin 4")
pinint = Pin(4, Pin.IN, Pin.PULL_UP)
pinint.irq(handler=pinint_toggle, trigger=Pin.IRQ_FALLING)


sensor.set_spectral_interrupt(True)

sensor.set_atime(29)                # 30 ASTEPS
sensor.set_astep(599)               # 1.67 ms
sensor.set_again(4)                 # factor 8 (with pretty much light)

try:
    while True:
        sensor.clear_interrupt()
        print("After clear_interrupt")
        print("pinint is", "high" if pinint.value() else "low")
        sensor.start_measure("F1F4CN")
        _,_,_,_,clear,_ = sensor.get_spectral_data()
        print("After reading measurements")
        print("Clear {:d}".format(clear))
        if sensor.check_interrupt():
            print("Interrupt detected!")
        else:
            print("no interrupts ....")
        print("pinint is", "high" if pinint.value() else "low")

        sleep_ms(2000)

except KeyboardInterrupt:
    print("Interrupted from keyboard")
    pinint.irq(handler=None)
    led.off()

#
