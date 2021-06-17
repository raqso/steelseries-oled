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
