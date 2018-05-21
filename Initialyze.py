__author__ = 'Martin'
import RPi.GPIO as GPIO
import Database

GPIO.setmode(GPIO.BCM)

ExistingRecords = Database.InitialPins.select()
if ExistingRecords.count():
   for ExistingRecord in ExistingRecords:
       #Database.InitialPins.select()
       print 'The Following Pins will be set: PIN: ' + str(ExistingRecord.Pin) + ' Value: ' + str(ExistingRecord.Value)
       print GPIO.setup(ExistingRecord.Pin,GPIO.OUT)
       print GPIO.output(ExistingRecord.Pin,ExistingRecord.Value)

