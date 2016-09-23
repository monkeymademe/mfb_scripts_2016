from gpiozero import AngularServo
import time
import explorerhat

s = AngularServo(18, min_angle=-0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000)

#servo = AngularServo(18, min_angle=45, max_angle=-45, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000)

s.angle = 50.0
speed = 60
wipes = 6
def wipe():
        s.angle = 25.0
        time.sleep(1)
        s.angle = 70.0
        time.sleep(1)


def bubbles(channel, event):
    if channel > 4:
        return
    if event == 'release':
        explorerhat.light[channel - 1].on()
	explorerhat.motor.one.forwards(99)
	time.sleep(2)
        explorerhat.motor.one.forwards(speed)
        for x in range(1, wipes):
		wipe()
        explorerhat.motor.stop()
	explorerhat.light[channel - 1].off()
	wipe()
	s.angle = 50.0

explorerhat.touch.released(bubbles)


def handle_input(pin):
    print(pin.name)


explorerhat.input.changed(handle_input)

explorerhat.pause()
