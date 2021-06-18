#!/usr/bin/env python3

from PIL import Image, ImageSequence

def get_image(path):
  return Image.open(path)

def convert_to_monochrome(image: Image):
	return image.convert('1')

def resize(image: Image):
	# Image size based on Apex 5 and 7
	return image.resize((128, 40))


def get_data_frame(frame: Image):
  frame = resize(frame)
  frame = convert_to_monochrome(frame)
  return frame.tobytes()
