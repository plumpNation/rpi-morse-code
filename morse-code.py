import RPi.GPIO as GPIO
import time

interval    = .25
shortDelay  = .25
longDelay   = .75

ON  = 1
OFF = 0

pinNumber = 18

code = '... --- ...'
sequence = list(code)

def setPin(state):
    GPIO.output(pinNumber, state)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinNumber, GPIO.OUT)
    setPin(OFF)
    wait(interval)

def teardown():
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
    teardown()
