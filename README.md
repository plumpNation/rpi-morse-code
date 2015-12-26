# rpi-morse-code
A small beginner's script for a morse code flasher using the RPi library in Python.

There is a commented version and an uncommented version.

## Setup

Setup your raspberry pi with an LED on an IO pin and a ground
pin, as per the example on the
[raspberry pi gpio intro](https://www.raspberrypi.org/documentation/usage/gpio/).

## To run

```shell
sudo python3 morse.py
```

## Testing

I included a small RPi.GPIO mock to just print some output,
it's not really useful unless you don't have a pi and just
want to play.

If you want to run using it, remember to comment out the line
that imports the RPi.GPIO module.
