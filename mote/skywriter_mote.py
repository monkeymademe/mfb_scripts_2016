#!/usr/bin/env python

import signal
import skywriter
from mote import Mote

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)


some_value = 5000

@skywriter.move()
def move(x, y, z):
  mote.clear()
  x = x*1000//4
  y = y*1000//4
  z = z*1000//4
  for channel in range(1, 5):
     for pixel in range(16):
         mote.set_pixel(channel, pixel, int(x), int(y), int(z))
  mote.show()

  print( x*1000//4, y*1000//4, z*1000//4 )

signal.pause()
