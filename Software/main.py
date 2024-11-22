import display
from machine import I2C, Pin
from time import sleep_ms
from as7341 import *  # Import the AS7341 sensor library
from m5stack import btnA  # Import the button

# Initialize I2C and AS7341 sensor
i2c = I2C(sda=Pin(32), scl=Pin(33))

sensor = AS7341(i2c)
if not sensor.isconnected():
    print("Failed to contact AS7341, terminating")
    sys.exit(1)

sensor.set_measure_mode(AS7341_MODE_SPM)
sensor.set_atime(29)                # 30 ASTEPS
sensor.set_astep(599)               # 1.67 ms
sensor.set_again(4)                 # factor 8 (with pretty much light)

# LED control functions
def set_led_current(current_mA):
    """Set the LED current in mA (range: 0 to 100 mA)."""
    sensor.set_led_current(current_mA)

def enable_led(enable):
    """Enable or disable the onboard LED."""
    sensor.enable_led(enable)

# Create the TFT display object
tft = display.TFT()

# Define custom colors
PURPLE = 0x800080
VIOLET = 0x9400D3

# Function to display the spectral data as a bar graph
def display_spectrum(f1, f2, f3, f4, f5, f6, f7, f8):
    tft.clear(tft.BLACK)

    # Scale the values to fit on the screen
    max_val = max(f1, f2, f3, f4, f5, f6, f7, f8)
    scale = 150 / max_val if max_val > 0 else 1

    # Adjust the bar width and spacing to fit the screen
    bar_width = 12
    spacing = 5
    start_x = (135 - (8 * bar_width + 7 * spacing)) // 2

    bars = [f1, f2, f3, f4, f5, f6, f7, f8]
    colors = [VIOLET, PURPLE, tft.BLUE, tft.CYAN, tft.GREEN, tft.YELLOW, tft.ORANGE, tft.RED]

    for i, bar in enumerate(bars):
        height = int(bar * scale)
        color = colors[i]
        tft.rect(start_x + i * (bar_width + spacing), 240 - height, bar_width, height, color, color)
        tft.font(tft.FONT_DefaultSmall)
        tft.text(start_x + i * (bar_width + spacing), 240 - height - 15, str(bar), tft.WHITE)

try:
    while True:
        if btnA.wasPressed():  # Check if the button is pressed
            print("Turning on LED")
            set_led_current(25)  # Set LED current to 25mA
            enable_led(True)

            # Perform spectral measurement
            sensor.start_measure("F1F4CN")
            f1, f2, f3, f4, clr, nir = sensor.get_spectral_data()
            sensor.start_measure("F5F8CN")
            f5, f6, f7, f8, clr, nir = sensor.get_spectral_data()

            display_spectrum(f1, f2, f3, f4, f5, f6, f7, f8)

            print("Turning off LED")
            enable_led(False)  # Turn off the LED after measurement
        sleep_ms(100)

except KeyboardInterrupt:
    print("Interrupted from keyboard")

sensor.disable()
