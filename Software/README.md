# micropython-as7341

@Chinna Devarapu
- Adapted for M5StickC using bottom I2C sensor port
- Added LED control support for DF Robots AS7341 sensor
- Added example for saving spectral data as text (save_data.py)
- Main functionality in main.py: displays spectral data as bar graph with count values above bars
- Developed using Thonny IDE

Original MicroPython driver by Rob Hamerling (Version 0.0, September 2022)
- Class for AS7341: 11 Channel Multi-Spectral Digital Sensor
- Adapted from WaveShare's Raspberry Pi implementation
- Source: https://www.waveshare.com/w/upload/b/b3/AS7341_Spectral_Color_Sensor_code.7z

## Modifications from Original
- Required specification of active I2C interface
- Pythonized implementation
- Optimized function names and I2C communications
- Improved code readability
- Added documentation strings

## Getting Started
- Use Micropython device with hardware I2C (e.g. ESP32)
- Connect AS7341 board via I2C interface
- Copy required files:
  - as7341.py
  - as7341_smux_select.py
- For GPIO examples: Connect GPIO pin to +3.3V (10K resistor) and pushbutton to GND

## Examples
- all_channels.py: read whole range of channels
- flicker.py: read flicker
- gpio_in_en.py: show use of GPIO pin for input
- interrupt.py: use of interrupt pin
- led_blink_pwm: show control of onboard LED
- pinint.py: use pin to trigger read-out
- syns.py: syns-mode, measurement starts with GPIO transition

## Documentation
- AS7341_AN000666_1-01.pdf - Application Note: SMUX Configuration
- AS7341_DS000504_3-00.pdf - Datasheet: 11-Channel Multi-Spectral Digital Sensor

Note: Repository is work in progress.
