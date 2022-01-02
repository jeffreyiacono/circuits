#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import wave
import pygame

# Set GPIO17 as LED pin
OpenLedPin = 17
# Set GPIO27 as OFF LED pin
ClosedLedPin = 27
# Set GPIO18 as Reed Switch pin
SwitchPin = 18

# Define a setup function for some setup
def setup():
	# Set up LoZ "secret found" sound file
	sound_filepath = '/home/pi/Documents/LOZ_Secret.wav'
	sound_file = wave.open(sound_filepath)
	sound_frequency = sound_file.getframerate()
	pygame.mixer.quit()
	pygame.mixer.init(frequency=sound_frequency)
	pygame.mixer.music.load(sound_filepath)
	# Set the GPIO modes to BCM Numbering
	GPIO.setmode(GPIO.BCM)
	# Set LedPin's mode to output,
	# and initial level to high (3.3v), ie. OFF
	GPIO.setup(OpenLedPin, GPIO.OUT, initial=GPIO.HIGH)
	# Set OFF LedPin's mode to output,
	# and initial level to high (3.3v), ie. OFF
	GPIO.setup(ClosedLedPin, GPIO.OUT, initial=GPIO.HIGH)
	# Set SwitchPin's mode to input,
	# and pull up to high (3.3V)
	GPIO.setup(SwitchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	# Set up a falling detect on SwitchPin,
	# and callback function to swLed
	GPIO.add_event_detect(SwitchPin, GPIO.FALLING, callback=switchChangedFn, bouncetime=250)

# Define a function for switch change callback
def switchChangedFn(ev=None):
	if GPIO.input(SwitchPin) == 0:
		print('SWITCH OPEN')
		print('LED ON ...')
		print('Playing Legend of Zelda "secret found" sound ...')
		GPIO.output(OpenLedPin, GPIO.LOW)
		GPIO.output(ClosedLedPin, GPIO.HIGH)
		pygame.mixer.music.play()
	else:
		print('SWITCH CLOSED')
		print('LED OFF ...')
		GPIO.output(OpenLedPin, GPIO.HIGH)
		GPIO.output(ClosedLedPin, GPIO.LOW)

# Define a main function for main process
def main():
	while True:
		# Don't do anything.
		time.sleep(1)

# Define a destroy function for clean up everything after
# the script finished
def destroy():
	pygame.mixer.quit()
	# Turn off LED
	GPIO.output(OpenLedPin, GPIO.HIGH)
	GPIO.output(ClosedLedPin, GPIO.HIGH)
	# Release resource
	GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
	setup()
	try:
		main()
	# When 'Ctrl+C' is pressed, the program
	# destroy() will be  executed.
	except KeyboardInterrupt:
		destroy()
