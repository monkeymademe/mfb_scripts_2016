from time import sleep
import imageprint



import dothat.touch as j
import dothat.lcd as l
import dothat.backlight as b
import signal

"""
Captouch provides the @captouch.on() decorator
to make it super easy to attach handlers to each button.

It's also a drop-in replacement for joystick, with one exception:
it has a "cancel" method.

The handler will receive "channel" ( corresponding to a particular
button ID ) and "event" ( corresponding to press/release ) arguments.
""" 

l.clear()
b.rgb(0, 0, 255)
l.write("Waiting!")


def druck():
	imageprint.print_img("makerfaire_print.png")

@j.on(j.BUTTON)
def handle_button(ch, evt):
    	print("Button pressed!")
    	l.clear()
    	b.rgb(255, 255, 255)
    	l.write("Printing!")
	druck()
	l.clear()
        b.rgb(255, 0, 238)
        l.write("Done!")	
	sleep(3)
	l.clear()
	b.rgb(0, 0, 255)
	l.write("Waiting!")

signal.pause()
