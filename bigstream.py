#!/usr/bin/env python

# Ported from:
# https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py


import os
import sys
if os.name != 'posix':
    sys.exit('platform not supported')
import psutil

from datetime import datetime
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont
import sys
import psutil
import time

font = ImageFont.load_default()
device = ssd1306(port=4, address=0x3C)
fontsize = 12
font = ImageFont.load_default()
font2 = ImageFont.truetype('../fonts/C&C Red Alert [INET].ttf', 32)
fontsmall = ImageFont.truetype('../fonts/C&C Red Alert [INET].ttf', fontsize)
line1 = psutil.disk_io_counters(perdisk=False).read_bytes
line2 = psutil.disk_io_counters(perdisk=False).write_bytes
ycoord = 0
inc_line = '0'
while True:
	ycoord = 0
	arraylines = []
	while ycoord <= 50:
		inc_line = sys.stdin.readline().strip()
		if inc_line == '':
			break
		arraylines.append(inc_line)
		with canvas(device) as draw:
			tmpcoord = 14
			for line in arraylines:
				if tmpcoord == 0:
					draw.text((0, 0), line, font=fontsmall, fill=255)
					tmpcoord = 14
				else: 
					draw.text((0, tmpcoord), line, font=fontsmall, fill=255)
					tmpcoord += fontsize
		if ycoord == 0:
			ycoord = 14
		else:
			ycoord += fontsize
		if ycoord > 50:
			break
	if inc_line == '':
		break
