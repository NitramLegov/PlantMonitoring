
__author__ = 'Martin'
import Database

import peewee
from peewee import *

def setup():
    Answer = raw_input("Does the Database need to be reinitialized?[Y/N] ")
    if Answer == "Y" or Answer == "y":
        Database.setup("Y")

    print '-----------------------------------------------'
    print 'Checking & Updating General Settings'
    ExistingRecords = Database.Settings.select()
    if ExistingRecords.count():
        print 'The Following records have been found:'
        for ExistingRecord in ExistingRecords:
            print 'ID: ' + str(ExistingRecord.ID) + ' Number of Columns: ' + str(ExistingRecord.NumberOfColumns) + ' Number of Rows: ' + str(ExistingRecord.NumberOfRows)
    Answer = raw_input("Which record do you want to create? Enter \'new\' for a new record.")
    if Answer == 'new' or Answer == 'New':
        Entry = Database.Settings()
        Entry.NumberOfColumns = raw_input("How Many Rows do you have?")
        Entry.NumberOfRows = raw_input("How Many Columns do you have?")
        print Entry.save()
    elif Answer.isdigit():
        Entry = Database.Settings.get(ID = int(Answer))
        Entry.NumberOfColumns = raw_input("How Many Rows do you have?")
        Entry.NumberOfRows = raw_input("How Many Columns do you have?")
        Entry.save()
    else:
        print 'Skipping this step.'
        #exit()

    print 'Setting have successfully been updated.'
    print '-----------------------------------------------'
    print 'Checking Sensor Types'
    ExistingRecords = Database.SensorTypes.select()
    if ExistingRecords.count():
        print 'The Following records have been found:'
        for ExistingRecord in ExistingRecords:
            #Database.SensorTypes.select()
            print 'ID: ' + str(ExistingRecord.ID) + ' SensorType: ' + str(ExistingRecord.SensorType) + ' HowToRead: ' + str(ExistingRecord.HowToRead)
    Answer = raw_input("Which record do you want to create? Enter \'new\' for a new record.")
    if Answer == 'new' or Answer == 'New':
        Entry = Database.SensorTypes()
        Entry.SensorType = raw_input("What Kind of Sensor is this?")
        Entry.HowToRead = raw_input("Which Function Module is used to read the Sensor?")
        Entry.SensorSpecificField1 = raw_input("Please enter the Value for the sensor specific field 1.")
        Entry.SensorSpecificField2 = raw_input("Please enter the Value for the sensor specific field 2.")
        Entry.SensorSpecificField3 = raw_input("Please enter the Value for the sensor specific field 3.")
        print Entry.save()
    elif Answer.isdigit():
        Entry = Database.SensorTypes.get(ID = int(Answer))
        Entry.SensorType = raw_input("What Kind of Sensor is this?")
        Entry.HowToRead = raw_input("Which Function Module is used to read the Sensor?")
        Entry.SensorSpecificField1 = raw_input("Please enter the Value for the sensor specific field 1.")
        Entry.SensorSpecificField2 = raw_input("Please enter the Value for the sensor specific field 2.")
        Entry.SensorSpecificField3 = raw_input("Please enter the Value for the sensor specific field 3.")
        Entry.save()
    else:
        print 'Skipping this step.'
        #exit()
    print 'Sensor types have successfully been updated.'
    print '-----------------------------------------------'
    print 'Checking initial Pins.'
    ExistingRecords = Database.InitialPins.select()
    if ExistingRecords.count():
        print 'The Following records have been found:'
        for ExistingRecord in ExistingRecords:
            #Database.InitialPins.select()
            print 'PIN: ' + str(ExistingRecord.Pin) + ' Value: ' + str(ExistingRecord.Value)
    Answer = raw_input("Which record do you want to create? Enter \'new\' for a new record.")
    if Answer == 'new' or Answer == 'New':
        Entry = Database.InitialPins()
        print Entry
        Entry.Pin = raw_input("Which Pin are we talking about (please use the BCM Number)?")
        Entry.Value = raw_input("Which Value should it have?")
        print Entry.save()
    elif Answer.isdigit():
        Entry = Database.InitialPins().get(Pin = int(Answer))
        Entry.Pin = raw_input("Which Pin are we talking about (please use the BCM Number)?")
        Entry.Value = raw_input("Which Value should it have?")
        Entry.save()
    else:
        print 'Skipping this step.'
        #exit()


if __name__ == '__main__':
    test = {'SETUP':setup}
    test['SETUP']()