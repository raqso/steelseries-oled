#!/usr/bin/env python3

from typing import Final
from cli import setup_close_handler
from PIL import Image, ImageFont, ImageDraw
from time import sleep
from device import getDevice, send_feature_report
import psutil

# use a truetype font
FONT_NAME: Final = "OpenSans-Regular.ttf"
FONT_SIZE: Final = 12

dev = getDevice()
setup_close_handler()
dev.open()

im = Image.new('1', (128,40))
draw = ImageDraw.Draw(im)

while(1):
    draw.rectangle([(0,0),(128,40)], fill=0)
    font = ImageFont.truetype(FONT_NAME, FONT_SIZE)

    cpu_freq, cpu_min, cpu_max = psutil.cpu_freq()

    draw.text((0, 0), "CPU: {:2.0f}%, {:2d} cores".format(psutil.cpu_percent(interval=1), psutil.cpu_count()), font=font, fill=255)
    draw.text((0, 12), "CPU Freq: {:4.0f}MHz".format(cpu_freq), font=font, fill=255)
    draw.text((0, 24), "Memory: {:2.0f}% Used".format(psutil.virtual_memory().percent), font=font, fill=255)

    data = im.tobytes()
    send_feature_report(dev, data)

    sleep(0.1)

dev.close()
