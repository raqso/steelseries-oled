from time import sleep
from image import get_data_frame
from PIL.Image import Image
from easyhid import Enumeration
import sys

def getDevice():
  # Stores an enumeration of all the connected USB HID devices
  en = Enumeration()

  # Return a list of devices based on the search parameters / Hardcoded to Apex 5
  devices = en.find(manufacturer="SteelSeries",
                    product="SteelSeries Apex 5")
  if not devices:
      devices = en.find(vid=0x1038, pid=0x1618, interface=1)
  if not devices:
      print("No devices found, exiting.")
      sys.exit(0)

  # Use first device found with vid/pid
  return devices[1]

def send_feature_report(dev, data):
    # Set up feature report package
    data = bytearray([0x61]) + data + bytearray([0x00])

    dev.send_feature_report(data)

def display_frame(dev, frame: Image):
	data = get_data_frame(frame)

	send_feature_report(dev, data)
	sleep(frame.info['duration'] / 1000)
