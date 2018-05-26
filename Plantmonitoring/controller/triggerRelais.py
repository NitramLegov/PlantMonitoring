from __future__ import print_function
import time
import datetime

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    running_on_pi = True
except:
    running_on_pi = False

def trigger_direct(pin,time_in_sec):
    if running_on_pi:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)
        print('Triggerring Relais at: %s' % (str(datetime.datetime.now())))
        GPIO.output(pin,GPIO.LOW)
        time.sleep(time_in_sec)
        GPIO.output(pin,GPIO.HIGH)
    else:
        print('Not running on a pi. The Relais on pin %i would have been triggered for %i seconds at %s' % (pin, time_in_sec, str(datetime.datetime.now())))

def trigger_behind_MCP23017(address, pin, time_in_sec):
    if running_on_pi:
        from controller.Adafruit_MCP230xx import Adafruit_MCP230XX
        mcp = Adafruit_MCP230XX(address,16,1)
        mcp.config(pin, Adafruit_MCP230XX.OUTPUT)
        mcp.output(pin,0)
        time.sleep(time_in_sec)
        mcp.output(pin,1)