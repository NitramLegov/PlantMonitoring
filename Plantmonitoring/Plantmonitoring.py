from __future__ import print_function
import web
from routes.index import Index
from routes.settings import Settings
import time
import controller.settings as settings
import json

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    running_on_pi = True
except:
    running_on_pi = False

PossibleUrls = (
                '/api/settings', 'Settings',
                '/api/settings/(.*)/(.*)', 'Settings',
                '/api/settings/(.*)', 'Settings',
                '/favicon.ico', 'Favicon',
                '/(.*)', 'Index',
                '/', 'Index'
)

host = settings.configuration.get('Server','host')
port_num = settings.configuration.getint('Server','port')

def cleanup():
    print('cleaning up before exit..')
    if running_on_pi:
        GPIO.cleanup()
    else:
        print('Not running on a raspberry pi. There is nothing to cleanup.')

def initialSetup():
    try:
        high_pins = json.loads(settings.configuration.get('Initial Pins', 'high'))
        for pin in high_pins:
            if running_on_pi:
                GPIO.setup(pin[1], GPIO.OUT, initial=GPIO.HIGH)
                GPIO.output(pin[1],GPIO.HIGH)
            else:
                print('Not running on a pi. Pin %i would have been set to high' % pin[1])
    except:
        print('No Pins to set to high or an error occurred')
    try:
        low_pins = json.loads(settings.configuration.get('Initial Pins', 'low'))
        for pin in low_pins:
            if running_on_pi:
                GPIO.setup(pin[1], GPIO.OUT, initial=GPIO.LOW)
                GPIO.output(pin[1],GPIO.LOW)
            else:
                print('Not running on a pi. Pin %i would have been set to low' % pin[1])
    except:
        print('No Pins to set to low or an error occurred')

if __name__ == "__main__":
    Server = web.application(PossibleUrls,globals())
    try:
        initialSetup()
        web.httpserver.runsimple(Server.wsgifunc(), (host, port_num))
    except Exception as e:
        print('An Error occurred:\n' + str(e))
        time.sleep(5)
    finally:
        cleanup()
