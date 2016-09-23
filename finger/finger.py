#!/usr/bin/env python
# coding: latin-1

# Import the libraries we need
import UltraBorg
import time
from gpiozero import Button

import colorsys
from blinkt import set_clear_on_exit, set_brightness, set_pixel, show


spacing = 360.0 / 16.0
hue = 0

set_clear_on_exit()
set_brightness(0.1)

button = Button(4)


# Settings
servoMin = -1.0                 # Smallest servo position to use
servoMax = +1.0                 # Largest servo position to use
startupDelay = 0.5              # Delay before making the initial move
stepDelay = 0.1                 # Delay between steps
rateStart = 0.05                # Step distance for all servos during initial move
rateServo1 = 0.01               # Step distance for servo #1
rateServo2 = 0.02               # Step distance for servo #2
rateServo3 = 0.04               # Step distance for servo #3
rateServo4 = 0.03               # Step distance for servo #4

# Start the UltraBorg
UB = UltraBorg.UltraBorg()      # Create a new UltraBorg object
UB.Init()                       # Set the board up (checks the board is connected)

def moveit():
    global servo1
    servo1 += rateServo4
    print servo1
    hue = int(time.time() * 100) % 360
    if servo1 > -0.9:
        set_pixel(7,165,0,38)
	show()
    if servo1 > -0.75:
        set_pixel(6,215,48,39)
        show()
    if servo1 > -0.5:
        set_pixel(5,244,109,67)
        show()
    if servo1 > -0.25:
        set_pixel(4,253,174,97)
        show()
    if servo1 > 0.0:
        set_pixel(3,254,224,139)
        show()
    if servo1 > 0.25:
        set_pixel(2,255,255,191)
        show()
    if servo1 > 0.5:
        set_pixel(1,224,243,248)
        show()
    if servo1 > 0.9:
        set_pixel(0,171,217,233)
        show()

# Loop over the sequence until the user presses CTRL+C
print 'Press CTRL+C to finish'
try:
    print 'Move to central'
    # Initial settings
    servo1 = 0.0
    servo2 = 0.0
    # Set our initial servo positions
    UB.SetServoPosition1(servo1)
    UB.SetServoPosition2(servo2)
    # Wait a while to be sure the servos have caught up
    time.sleep(startupDelay)
    print 'Sweep to start position'
    while servo1 > servoMin:
        # Reduce the servo positions
        servo1 -= rateStart
	servo2 -= rateStart
        # Check if they are too small
        if servo1 < servoMin:
            servo1 = servoMin
	    servo2 = servoMax
        # Set our new servo positions
        UB.SetServoPosition1(servo1)
	UB.SetServoPosition2(servo2)
        # Wait until the next step
        time.sleep(stepDelay)
    print 'Sweep all servos through the range'
    #while servo1 < servoMax:
    while True:
	if servo1 < servoMin:
            servo1 = servoMin
	if servo1 < servoMax and servo1 > servoMin:
		servo1 -= rateServo2
		if servo1 < -0.9:
        		set_pixel(7,0,0,0)
        		show()
    		if servo1 < -0.75:
		        set_pixel(6,0,0,0)
        		show()
    		if servo1 < -0.5:
        		set_pixel(5,0,0,0)
		        show()
    		if servo1 < -0.25:
		        set_pixel(4,0,0,0)
        		show()
    		if servo1 < 0.0:
		        set_pixel(3,0,0,0)
        		show()
    		if servo1 < 0.25:
		        set_pixel(2,0,0,0)
			show()
		if servo1 < 0.5:
		        set_pixel(1,0,0,0)
        		show()
    		if servo1 < 0.9:
		        set_pixel(0,0,0,0)
        		show()

	button.when_released = moveit
        # Increase the servo positions at separate rates
        #servo1 += rateServo1
        # Check if any of them are too large, if so wrap to the over end
        if servo1 > servoMax:
            servo1 -= (servoMax - servoMin)
	    servo2 = servoMin
	    UB.SetServoPosition2(servo2)
	    i = 0
	    while i < 550:
		hue = int(time.time() * 100) % 360
		for x in range(8):
			offset = x * spacing
			h = ((hue + offset) % 360) / 360.0
			r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
			set_pixel(x,r,g,b)
		show()
		i = i + 1
		if i == 100:
			servo1 = servoMin
			UB.SetServoPosition1(servo1)
		if i == 200:
			servo1 = servoMax
			UB.SetServoPosition1(servo1)
		if i == 300:
                        servo1 = servoMin
                        UB.SetServoPosition1(servo1)
                if i == 400:
                        servo1 = servoMax
                        UB.SetServoPosition1(servo1)
		if i == 500:
                        servo1 = servoMin
                        UB.SetServoPosition1(servo1)
		time.sleep(0.001)
	    servo2 = servoMax
            UB.SetServoPosition2(servo2)
	    for x in range(8):
                        set_pixel(x,0,0,0)
	    show()
        # Set our new servo positions
        UB.SetServoPosition1(servo1)
       # Wait until the next step
        time.sleep(stepDelay)
except KeyboardInterrupt:
    # User has pressed CTRL+C
    print 'Done'
