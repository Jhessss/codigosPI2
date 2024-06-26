import os
import glob
import time

# Base directory for the 1-Wire devices
base_dir = '/sys/bus/w1/devices/'

# Find the directory for the DS18B20 sensor
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as f:
        return f.readlines()

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

while True:
    temp_c = read_temp()
    print(f'Temperature: {temp_c:.2f}°C')
    time.sleep(1)
