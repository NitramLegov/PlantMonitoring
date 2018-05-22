from __future__ import print_function
import web
from routes.index import Index
from routes.settings import Settings
import time
import controller.settings as settings

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
    try:
        import RPi.GPIO as GPIO
        GPIO.cleanup()
    except:
        print('nothing')

if __name__ == "__main__":
    Server = web.application(PossibleUrls,globals())
    try:
        web.httpserver.runsimple(Server.wsgifunc(), (host, port_num))
    except Exception as e:
        print('An Error occurred:\n' + str(e))
        time.sleep(5)
    finally:
        cleanup()
