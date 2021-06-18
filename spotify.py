# - coding: UTF-8 -
from device import getDevice, send_feature_report
from typing import Final
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from urllib.parse import urlparse
from PIL import Image, ImageFont, ImageDraw

def draw_song_info(status, title, artist):
	FONT_NAME: Final = "OpenSans-Regular.ttf"

	dev = getDevice()
	dev.open()

	im = Image.new('1', (128, 40))
	draw = ImageDraw.Draw(im)

	draw.rectangle([(0, 0), (128, 40)], fill=0)

	font14 = ImageFont.truetype(FONT_NAME,14)
	font12 = ImageFont.truetype(FONT_NAME,12)

	first_line = ('|| ' if status == 'Paused' else '') + title
	second_line = artist

	draw.text((0, 0), first_line, font=font14, fill=255)
	draw.text((0, 18), second_line, font=font12, fill=255)
	draw.rectangle([(0, 38), (128, 40)], fill="#ffffff")

	data = im.tobytes()
	send_feature_report(dev, data)

	dev.close()


def replace_image_host(image_url):
  parsed = urlparse(image_url)
  parsed = parsed._replace(netloc="i.scdn.co").geturl()
  return parsed

def handler_cond(*args):
	eventData = args[1]
	status = eventData.get('PlaybackStatus')
	metadata = eventData.get('Metadata')

	song_title = metadata['xesam:title']
	artist = ", ".join(metadata['xesam:artist'])
	image = replace_image_host(metadata['mpris:artUrl'])

	draw_song_info(status, song_title, artist)

DBusGMainLoop(set_as_default=True)

loop = GLib.MainLoop()
session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                     "/org/mpris/MediaPlayer2")

spotify_bus.connect_to_signal("PropertiesChanged", handler_cond)

loop.run()
