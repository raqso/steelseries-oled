#!/usr/bin/env python3

from cli import setup_close_handler
from image import  get_image
from PIL import ImageSequence
from device import display_frame, getDevice
import sys

def validate_arguments():
    if(len(sys.argv) < 2):
     print("Usage: oled.py image.gif\n")
     sys.exit(0)

validate_arguments()
dev = getDevice()
setup_close_handler()
dev.open()
image = get_image(sys.argv[1])

while(1):
	for frame in ImageSequence.Iterator(image):
	    display_frame(dev, frame)

dev.close()
