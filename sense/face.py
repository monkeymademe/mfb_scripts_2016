from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

Y = [255, 255, 0]  # Yellow
W = [255, 255, 255]  # White
B = [0, 0, 0] # Black
P = [234, 120, 152] # Pink

blank = [
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y
]

happy = [
Y, Y, Y, Y, Y, Y, Y, Y,
Y, B, Y, Y, Y, Y, B, Y,
B, Y, B, Y, Y, B, Y, B,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, W, W, W, W, W, W, Y,
Y, B, B, B, B, B, B, Y,
Y, Y, B, P, P, B, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y
]

smile = [
Y, Y, Y, Y, Y, Y, Y, Y,
Y, W, W, Y, Y, W, W, Y,
Y, W, B, Y, Y, B, W, Y,
Y, W, W, Y, Y, W, W, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, B, Y, Y, Y, Y, B, Y,
Y, Y, B, B, B, B, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y
]

wink = [
Y, Y, Y, Y, Y, Y, Y, Y,
Y, W, W, Y, Y, Y, B, Y,
Y, W, B, Y, Y, B, Y, Y,
Y, W, W, Y, Y, Y, B, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, B, Y, Y, Y, Y, B, Y,
Y, Y, B, B, B, B, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y
]

woah = [
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, W, Y, Y, W, Y, Y,
Y, W, B, Y, Y, B, W, Y,
Y, W, W, Y, Y, W, W, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, P, Y, B, B, Y, P, Y,
Y, Y, Y, B, B, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y
]

event = sense.stick.wait_for_event()
if event.action == "released":
  sense.set_pixels(smile)
  sleep(0.5)
  sense.set_pixels(wink)
  sleep(0.5)
  sense.set_pixels(smile)
  i = 0
  while i = 5:
    orientation = sense.get
