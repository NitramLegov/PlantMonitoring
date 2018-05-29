#!/usr/bin/python
from __future__ import print_function
import smbus

class Plant_Helper(object):
    """description of class"""
    thread = None  # background thread
    next_event = None
    time_of_next_event = None
    obs = ephem.Observer()
    obs.lat = '49.10318'
    obs.long = '8.47589'
    def initialize(self):
        if Plant_Helper.thread is None:
            # start background thread
            Plant_Helper.thread = threading.Thread(target=self._thread)
            Plant_Helper.thread.daemon = True
            Plant_Helper.thread.start()
            # wait until the next event got calculated
            while self.next_event is None or self.time_of_next_event is None:
                time.sleep(0)

    def get_next_event(self):
        self.initialize()
        return 'Next Event: ' + Plant_Helper.next_event + ' at: ' + str(Plant_Helper.time_of_next_event)


    @classmethod
    def _thread(cls):
        obs = Plant_Helper.obs
        obs.date = datetime.datetime.utcnow()
        if obs.next_rising(ephem.Sun()) < obs.next_setting(ephem.Sun()):
            #it is night, close door
            Plant_Helper.next_event = 'Sunrise'
            Plant_Helper.time_of_next_event = ephem.localtime(obs.next_rising(ephem.Sun()))
            print 'Initializing... It is night, so the door needs to be closed.'
            controller.door.down()
        else:
            #it is day, open door
            Plant_Helper.next_event = 'Sunset'
            Plant_Helper.time_of_next_event = ephem.localtime(obs.next_setting(ephem.Sun()))
            print 'Initializing... It is day, so the door needs to be open.'
            controller.door.up()
        while (True):
            obs.date = datetime.datetime.utcnow()
            #Testing line: 3 Seconds until Sunrise
            #obs.date = ephem.Date('2018/04/23 04:19:22.00')
            #Testing line: 10 Seconds until Sunset
            #obs.date = ephem.Date('2018/04/23 18:30:15.00')
            if obs.next_rising(ephem.Sun()) < obs.next_setting(ephem.Sun()):
                #it is night, next event is the sunrise
                Plant_Helper.next_event = 'Sunrise'
                Plant_Helper.time_of_next_event = ephem.localtime(obs.next_rising(ephem.Sun()))
                time_to_sleep = (obs.next_rising(ephem.Sun()).datetime() - obs.date.datetime()).total_seconds()
            else:
                #it is day, next event is the sunset
                Plant_Helper.next_event = 'Sunset'
                Plant_Helper.time_of_next_event = ephem.localtime(obs.next_setting(ephem.Sun()))
                time_to_sleep = ((obs.next_setting(ephem.Sun()).datetime() - obs.date.datetime())).total_seconds()

            if Plant_Helper.next_event  == 'Sunrise':
                print "Currently it is nighttime. The door would go up at: " + str(ephem.localtime(obs.next_rising(ephem.Sun())))
                print "This means in " + str(((obs.next_rising(ephem.Sun()).datetime() - obs.date.datetime())).total_seconds()) + " seconds"
                time.sleep(time_to_sleep)
                controller.door.up()
            else:
                print "Currently it is daytime. The door would go down at: " + str(ephem.localtime(obs.next_setting(ephem.Sun())))
                print "This means in " + str(((obs.next_setting(ephem.Sun()).datetime() - obs.date.datetime())).total_seconds()) + " seconds"
                time.sleep(time_to_sleep)
                controller.door.down()