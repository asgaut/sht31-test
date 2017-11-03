# This is a Python 3 upgrade of:
# https://github.com/ControlEverythingCommunity/SHT31/blob/master/Python/SHT31.py

# Datasheet from Sensirion for address and command information:
# https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital.pdf

import smbus2 as smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# SHT31 address, 0x44
# Send measurement command, 0x2C
# High repeatability measurement, 0x06
bus.write_i2c_block_data(0x44, 0x2C, [0x06])

time.sleep(0.5)

# SHT31 address, 0x44
# Read data back from 0x00, 6 bytes
# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
data = bus.read_i2c_block_data(0x44, 0x00, 6)

# Convert the data
temp_C = -45 + (175 * (data[0] * 256 + data[1]) / 65535.0)
temp_F = -49 + (315 * (data[0] * 256 + data[1]) / 65535.0)
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

# Output data to screen
print("Temperature in Celsius is: {0:.2f} C".format(temp_C))
print("Temperature in Fahrenheit is: {0:.2f} C".format(temp_F))
print("Relative Humidity is: {0:.2f} %RH".format(humidity))
