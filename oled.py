#!/usr/bin/env python3

from PIL import Image, ImageSequence
from easyhid import Enumeration
from time import sleep
from device import getDevice
import signal
import sys

def signal_handler(sig, frame):
    try:
    	# Blank screen on shutdown
        dev.send_feature_report(bytearray([0x61] + [0x00] * 641))
        dev.close()
        print("\n")
        sys.exit(0)
    except:
        sys.exit(0)

# Check for arguments
if(len(sys.argv) < 2):
	print("Usage: oled.py image.gif\n")
	sys.exit(0)

# Set up ctrl-c handler
signal.signal(signal.SIGINT, signal_handler)

dev = getDevice()

print("Press Ctrl-C to exit.\n")
dev.open()

im = Image.open(sys.argv[1])

while(1):
	for frame in ImageSequence.Iterator(im):

	    # Image size based on Apex 5 and 7
	    frame = frame.resize((128, 40))

	    # Convert to monochrome
	    frame = frame.convert('1')
	    data = frame.tobytes()

	    # Set up feature report package
	    data = bytearray([0x61]) + data + bytearray([0x00])

	    dev.send_feature_report(data)
	    sleep(frame.info['duration'] / 1000)

dev.close()
