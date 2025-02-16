# Pocket Spectrometer

![alt text](https://github.com/scientistnobee/Pocket-Spectrometer/blob/main/Images/IMG_6542.jpg width="150" height="280")

## The Vision

I've always wanted to create a spectrometer that is so small it can fit into one's pocket and just barely larger than a cuvette itself. Working with bulky commercial spectrometers in labs, I was wondering about applications of such a small spectrometer. That's when I discovered the perfect combination – the M5StickC microcontroller and the AS7341 spectral sensor. My goal was simple: create an ultra-compact spectrometer that anyone could use.

## Why This Matters

While commercial spectrometers offer high precision, they're often expensive, bulky, and require a computer connection. I wanted something different – a standalone device that could fit in your pocket, complete with its own display and interface, without requiring external equipment such as connection to a mobile app or a computer. The kind of tool that could democratize spectroscopy for educators, students, and citizen scientists.

## Bill of Materials (BOM)

* 1x M5StickC (https://docs.m5stack.com/en/core/m5stickc_plus) 
* 1x AS7341 spectral sensor  (https://www.dfrobot.com/product-2132.html)
* 1x Grove connector  (https://docs.m5stack.com/en/accessory/cable/grove_cable)
* 2x M2 screws  (https://eu.mouser.com/ProductDetail/Harwin/M80-2260000B?qs=DXv0QSHKF4wN5XPxPv8mDw%3D%3D&utm_source=octopart&utm_medium=aggregator&utm_campaign=855-M80-2260000B&utm_content=Harwin)
* 2x M2 heat-set inserts  (https://www.mouser.com/ProductDetail/SI/IUTFB-M2?qs=DPoM0jnrROVcA4QFWOCRzw%3D%3D&srsltid=AfmBOopUU4Yk4SA0-Q8_GQOYWdSUdiCuBDWbHyQfNmQKO6hRtp1Q_SV6)
* Black filament for 3D printing  
* White reflector (Optional)
![alt text](https://github.com/scientistnobee/Pocket-Spectrometer/blob/main/Images/IMG_6296.jpg)
## 3D-Printed Components

* Main body
* Cap

## Hardware Tools Required

* 3D printer  
* Soldering iron  
* Screwdriver

## Software Tools Required

* OpenSCAD for 3D printed parts (Optional, only required to modify the designs)  
* 3D printer slicer software (I used Ultimaker’s CURA)  
* Thonny IDE for programming


## Reasoning for choosing the particular Electronic Components

### AS7341 Spectral sensor: Advanced Spectral Sensing

The AS7341 sensor is crucial for this project:

* 11 readable individual sensor elements (10 light channels plus flicker detection)  
* Coverage from 350-1000 nm for comprehensive analysis  
* Built-in LED control for consistent illumination  
* Low power consumption for extended battery life  
* Affordable price point (\~$16)

### M5StickC: Portable but powerful mini computer

The M5StickC is the perfect platform for this project because it packs incredible functionality into a tiny package:

- Built-in rechargeable battery for true portability and for on-field applications  
- USB-C connector for easy charging and programming  
- Seeed Grove port for simple sensor connections  
- Two user-programmable buttons for interface control  
- TFT display screen for displaying spectra in real-time   
- Beautifully labeled breakout header for expansion  
- Extra in-bulit sensors (6-axis IMU, Microphone, IR transmitter)   
- Compact size (48.2 x 25.5 x 13.7mm) ideal for portable size of pocket spectrometer  
- MicroPython support for easy programming  
- Affordable price point (\~$20)

## Build Instructions

### Hardware Assembly

1. Cut the Grove connector to 15cm length and solder the wires  
![alt text](https://github.com/scientistnobee/Pocket-Spectrometer/blob/main/Images/IMG_6300.jpg)
2. Connect the Grove cable to the M5StickC  
3. Flash the firmware using Thonny  
4. Test the spectral sensor functionality  
5. Disconnect the Grove connector  
6. 3D print the main body and cap (no support required)  
7. Install M2 heat-set inserts using the soldering iron  ![alt text](https://github.com/scientistnobee/Pocket-Spectrometer/blob/main/Images/IMG_6298.jpg)

8. Mount the AMS sensor to the body using M2 screws  ![alt text](https://github.com/scientistnobee/Pocket-Spectrometer/blob/main/Images/IMG_6305.jpg)

9. Press-fit the M5StickC into the body from the top  
10. Connect the Grove connector from the bottom  
11. Apply black tape to cover the AMS sensor and wires
 ![alt text](https://github.com/scientistnobee/Pocket-Spectrometer/blob/main/Images/IMG_6542.jpg)
## Firmware Setup Instructions

### 1\. Prepare M5StickC

1. Power on the M5StickC  
2. Quickly press the M5 button after restart (using reset/PWR button) until you see the settings screen  
3. Select "Switch Mode" using the M5 button  
4. Choose "USB Mode" from the options

### 2\. Set Up Thonny IDE

1. Download and install [Thonny IDE](https://thonny.org/)  
2. Open Thonny  
3. Navigate to Tools \> Options \> Interpreter  
4. Configure settings:  
   - Set interpreter to "MicroPython (ESP32)"  
   - Select the correct COM port for your M5StickC  
   - Click OK and reconnect  
5. Once connected, you can write and test code directly in the IDE  
6. Best practice is to write your code in `main.py` for automatic execution on startup  
   

## Applications

The Pocket Spectrometer has numerous practical applications:

### Environmental Monitoring

* **Water Quality Testing**:  
  - Measure water turbidity  
  - Test chlorine content  
  - Monitor pH levels  
  - Assess water hardness  
  - Analyze phosphate content

### Biological Applications

* **Aquatic Habitat Monitoring**:  
  - Track ammonia levels  
  - Measure nitrate and nitrite concentrations  
  - Monitor phosphate levels  
  - Ideal for both freshwater and saltwater systems  
  - Perfect for aquaponics monitoring

### Environmental Testing

* **Soil Analysis**:  
  - Detect environmental pollutants  
  - Measure heavy metals like lead  
  - Test for oil contamination  
  - Monitor diesel presence  
  - Screen for pesticides

### Laboratory Use

* **Biochemical Analysis**:  
  - Protein quantification using Bradford assay  
  - Colorimetric enzyme assays  
  - Chemical concentration measurements  
  - Educational demonstrations  
  - STEM project applications

## Technical Implementation

The code is written in MicroPython for simplicity and accessibility, making it easy to modify for various applications. Most of the AI tools nowadays are good with python code, so would be handy to have the code in micropython.

## Future Work

* Upgrade to AS7343 as it has 14 spectral channels, compared to 10 spectral channels of  AS7341  
* Optimize battery life for extended field use  
* Conduct comprehensive testing (Work in progress)  
* Write the protocols in detail and make standard curve plots  
* Add saving the spectra as a time-stamped text file 

## Troubleshooting Tips for software

* If code doesn't execute properly, use the stop/rerun button in Thonny until you see three forward-looking arrows in the console  
* Restart the device if experiencing connection issues  
* Ensure proper USB mode selection before programming  
* Double-check Grove connector wiring if sensor readings are incorrect

