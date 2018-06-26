#!/usr/bin/python
from __future__ import print_function
import time
import threading
import datetime
import pynq

try:
    import smbus
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    running_on_pi = True
except:
    running_on_pi = False


class Plant_Helper(object):
    """description of class"""
    thread = None  # background thread
    next_event = None
    time_of_next_event = None
    Plant = None

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
        #do stuff here
        #calculate next event and wait until next event.
        current_time = datetime.datetime.now

        #This is only pseudocode so far!
        if Plant.WateringLogic = "Time":
            last_watering = get_last_watering()
            next_watering = last_watering + plant.WateringThreshold
            wait_time = next_watering - current_time
            if wait_time <= 0:
                water_now()
            else:
                time.sleep(wait_time)
