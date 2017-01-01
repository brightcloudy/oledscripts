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
font2 = ImageFont.truetype('./DroidSansMono.ttf', 18)
fontsmall = ImageFont.truetype('./DroidSansMono.ttf', 10)
fonthead = ImageFont.truetype('./DroidSansMono.ttf', 12)
ycoord = 14
prevline1 = ""
prevline2 = ""
while True:
	with canvas(device) as draw:
		draw.text((0, 0), " CPU%       MEM%", font=fonthead, fill=255)
		draw.text((0, 55), "%s %+05d" % (time.strftime("%a %d %b %Y"), time.timezone / 60 / 60 * -100), font=fontsmall, fill=255)
		draw.text((18, 34), time.strftime("%H:%M:%S"), font=font2, fill=255)
		draw.text((0, 14), "%04.1f%% %04.1f%%" % (psutil.cpu_percent(), psutil.virtual_memory().percent), font=font2, fill=127)
		time.sleep(1.00)
