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
        #do stuff here