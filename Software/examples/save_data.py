import sys
from m5stack import *
import time
from uiflow import *
from time import sleep_ms
from machine import I2C, Pin
# from datetime import datetime

i2c = I2C(sda=Pin(32), scl=Pin(33))

from as7341 import *

 # rtc.settime('ntp', host='cn.pool.ntp.org', tzone=1)
sensor = AS7341(i2c)
if not sensor.isconnected():
    print("Failed to contact AS7341, terminating")
    sys.exit(1)




sensor.set_measure_mode(AS7341_MODE_SPM)
sensor.set_atime(29)                # 30 ASTEPS
sensor.set_astep(599)               # 1.67 ms
sensor.set_again(4)                 # factor 8 (with pretty much light)

print("start saving data")
with open("spectral_data10.txt", "w") as f:
    f.write("f1,f2,f3,f4,f5,f6,f7,f8,clr,nir\n")
    print("f1,f2,f3,f4,f5,f6,f7,f8,clr,nir\n")
    
    try:
        while True:
            sensor.start_measure("F1F4CN")
            f1,f2,f3,f4,clr,nir = sensor.get_spectral_data()
            sensor.start_measure("F5F8CN")
            f5,f6,f7,f8,clr,nir = sensor.get_spectral_data()
            
            #  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            row = "{},{},{},{},{},{},{},{},{},{}\n".format(f1, f2, f3, f4, f5, f6, f7, f8, clr, nir)
            
            f.write(row)
            print(row)
            print("data saved")
            sleep_ms(10000)

    except KeyboardInterrupt:
        print("Interrupted from keyboard")

    sensor.disable()
