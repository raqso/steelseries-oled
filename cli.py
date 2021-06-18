from device import getDevice
import sys
import signal

def signal_handler(sig, frame):
  dev = getDevice()

  try:
      blank_screen = bytearray([0x61] + [0x00] * 641)
      dev.send_feature_report(blank_screen)
      dev.close()
      print("\n")
      sys.exit(0)
  except:
      sys.exit(0)

def setup_close_handler():
  # Set up ctrl-c handler
  signal.signal(signal.SIGINT, signal_handler)
