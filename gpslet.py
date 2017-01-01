#!/usr/bin/env python

# Ported from:
# https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py


import os
import sys
if os.name != 'posix':
    sys.exit('platform not supported')
import psutil
import serial
import io

from datetime import datetime
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont
import sys
import psutil
import time

ser = serial.Serial('/dev/ttyUSB1')
ser.write("$PMTK220,500*2B\r\n")
ser.write("$PMTK251,115200*1F\r\n")
ser.flush()
ser.close()
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=0.5)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser), newline=None)
sio.write(unicode("$PMTK314,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29\r\n"))
sio.flush()
font = ImageFont.load_default()
device = ssd1306(port=4, address=0x3C)

font = ImageFont.load_default()
font2 = ImageFont.truetype('../fonts/C&C Red Alert [INET].ttf', 20)
fontsmall = ImageFont.truetype('../fonts/C&C Red Alert [INET].ttf', 12)
line1 = psutil.disk_io_counters(perdisk=False).read_bytes
line2 = psutil.disk_io_counters(perdisk=False).write_bytes
ycoord = 14
prevline1 = ""
prevline2 = ""
while True:
	with canvas(device) as draw:
		line1 = sio.readline()
		print line1.strip()
	        stripline = line1.strip()
	        fields = stripline.split(',')
		if fields[0] == '$GPGGA':
			datestring = str(fields[1])
			hours = datestring[0:2]
			minutes = datestring[2:4]
			seconds = datestring[4:]
			prevline1 = "%s:%s:%s" % (hours, minutes, seconds)
			lat = float(fields[2])
			fixlat = lat / 100.0
			longitude = float(fields[4])
			fixlongitude = longitude / 100.0
			prevline2 = str(round(fixlat, 4)) 
			print "%s %s, %s %s" % (fixlat, fields[3], fixlongitude, fields[5])
			draw.text((0, 0), prevline1, font=fontsmall, fill=255)
			draw.text((0, 14), str(round(fixlat, 6)) + " " + fields[3], font=font2, fill=255)
			draw.text((0, 14+20), str(round(fixlongitude, 6)) + " " + fields[5], font=font2, fill=255)
