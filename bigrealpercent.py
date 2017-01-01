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

font = ImageFont.load_default()
font2 = ImageFont.truetype('../fonts/C&C Red Alert [INET].ttf', 32)
fontsmall = ImageFont.truetype('../fonts/C&C Red Alert [INET].ttf', 12)
line1 = psutil.disk_io_counters(perdisk=False).read_bytes
line2 = psutil.disk_io_counters(perdisk=False).write_bytes
ycoord = 14
while True:
	with canvas(device) as draw:
		draw.text((0, 0), "CPU", font=fontsmall, fill=255)
		draw.text((64, 0), "MEM", font=fontsmall, fill=255)
		draw.text((0, 14), str(psutil.cpu_percent(interval=0.1)), font=font2, fill=255)
		draw.text((64, 14), str(psutil.virtual_memory().percent), font=font2, fill=255)
