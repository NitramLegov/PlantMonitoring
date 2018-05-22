from __future__ import print_function
import time
import datetime
try:
    import RPi.GPIO as GPIO
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