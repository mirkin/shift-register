#!/usr/bin/python
'''
SN74HC505 shift register
Very simple shift register demo, hook up 8 LEDs and store the bit patterns in a
list of bytes.
'''

import RPi.GPIO as GPIO
import time

PIN_LATCH=35
PIN_DATA=36
PIN_CLOCK=37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LATCH,GPIO.OUT)
GPIO.setup(PIN_DATA,GPIO.OUT)
GPIO.setup(PIN_CLOCK,GPIO.OUT)

def showHex(byte):
    GPIO.output(PIN_LATCH,0)
    for x in range(8):
        GPIO.output(PIN_DATA,(byte>>x)&1)
        GPIO.output(PIN_CLOCK,1)
        GPIO.output(PIN_CLOCK,0)
    GPIO.output(PIN_LATCH,1)
list1=[0x80,0x40,0x20,0x10,0x08,0x04,0x02,0x01,0x02,0x04,0x08,0x10,0x20,0x40]
list2=[0x80,0xC0,0xE0,0xF0,0xF8,0xFC,0xFE,0xFF,0x7F,0x3F,0x1F,0x0F,0x07,0x03,0x01,0,0,0,0,0,0,0,0]
while True:
    for item in list2:
        showHex(item)
        time.sleep(0.03)


GPIO.cleanup()
