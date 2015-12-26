# morse code flasher for raspberry pi

# the GPIO module controls the pins.
# Make sure you remember to run the script as sudo
# example:
# sudo python3 morse.py
import RPi.GPIO as GPIO

# We'll use the time module to delay between dots and dashes.
import time

# This is a mock GPIO class for testing.
# If you comment out the RPi.GPIO import above, and uncomment this, you
# can run the code without the need for the pi.
# class GPIO():
#     BCM    = 'broadcom'
#     BOARD  = 'board'
#     OUT    = 'out'
#     IN     = 'in'
#
#     def output(pinNumber, state):
#         print("setting", pinNumber, "to the", state, "state")
#
#     def setmode(mode):
#         print("setting mode to", mode)
#
#     def setup(pinNumber, direction):
#         print("setting up pin", pinNumber, "to face", direction)
#
#     def cleanup():
#         print("cleaning up")

# Before each character is 'lit' we need a delay or the change between each
# character will be too quick, and will look really bad.
interval = .25

# For the dot...
shortDelay = .25

# For the dash...
longDelay = .75

# The pins on the pi will be turned on or off, lighting the LED
# By setting the 1 to ON and the 0 to OFF, we can write code that is easy to read.
ON = 1
OFF = 0

# This is the IO pin we will use to switch the LED on or off
pinNumber = 18

# this code could come from stdin or from a file, but for now it's easy to have it here
code = '... --- ...'

# break the code apart into a list, so we can loop through it
sequence = list(code)

# usage: setPin(ON) or setPin(OFF)
def setPin(state):
    GPIO.output(pinNumber, state)

def setup():
    # Set mode to `broadcom`, we could also set to `board`.
    # These are the two different numbering systems to refer to the pins by number.
    GPIO.setmode(GPIO.BCM)

    # Now we set up our pin to be an output pin. An example of an input would be a button.
    GPIO.setup(pinNumber, GPIO.OUT)

    # this isn't really necessary, the pin will be off by default
    setPin(OFF)

    # I want to wait before we start, just a little, just in case you are using a setup
    # that shows the off state as well as an LED for the on state.
    wait(interval)

def teardown():
    # Teardown means we are finished, and want to `cleanup` after ourselves.
    # GPIO provides us this method, and resets all the GPIO pins we have setup as inputs or outputs.
    GPIO.cleanup()

def wait(seconds):
    time.sleep(seconds)

def flash(seconds):
    setPin(ON)
    wait(seconds)
    setPin(OFF)
    wait(interval)

def dot():
    flash(shortDelay)

def dash():
    flash(longDelay)

def space():
    wait(longDelay)

# we create a dictionary of which function to run for each character
doActionFor = {
    '-': dash,
    '.': dot,
    ' ': space
}

try:
    setup()

    for character in sequence:
        doActionFor[character]()

    teardown()

except:
    # if an error happens we still want to cleanup after ourselves anyway
    teardown()
