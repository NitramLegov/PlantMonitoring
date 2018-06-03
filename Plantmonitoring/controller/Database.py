from __future__ import print_function
__author__ = 'Martin'

import peewee
from peewee import *
import controller.settings as settings

db_file = settings.configuration.get('SQLite','Database_file')
#db = MySQLDatabase('PLANTMONITORING',user="root",passwd="RaspberrySQL")
db = SqliteDatabase(db_file)

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db

class Garden(BaseModel):
    ID = PrimaryKeyField()
    Name = CharField()
    NumberOfColumns = IntegerField()
    NumberOfRows = IntegerField()

class Plants(BaseModel):
    ID = PrimaryKeyField()
    Location_Row = IntegerField()
    Location_Column = IntegerField()
    Name = CharField()
    WateringLogic = CharField()
    WateringTreshold = IntegerField()
    WateringSeconds = IntegerField()
#    LastWateringTime = TimeField(null=True)
    Garden = ForeignKeyField(Garden,to_field='ID')

class SensorTypes(BaseModel):
    SensorType = CharField(primary_key=True)
    HowToRead = CharField()
    SensorSpecificField1 = CharField()
    SensorSpecificField2 = CharField()
    SensorSpecificField3 = CharField()

class Sensors(BaseModel):
    ID = PrimaryKeyField()
    Type = ForeignKeyField(SensorTypes,to_field='SensorType')
    Location_Row = IntegerField()
    Location_Column = IntegerField()
    ChipToRead = IntegerField()
    LocationOnChip = IntegerField()
    EnablePin = IntegerField()
    PlantItIsRelevantFor = ForeignKeyField(Plants,to_field=ID)
    ForceReadingNextTime = BooleanField()

#class SensorValues(BaseModel):
#    Sensor = ForeignKeyField(Sensors,to_field='ID')
#    Timestamp = DateTimeField()
#    Value = IntegerField()
#    class Meta:
#        primary_key = CompositeKey('Sensor', 'Timestamp')

#class InitialPins(BaseModel):
#    ID = PrimaryKeyField()
#    Pin = IntegerField(unique=True)
#    Value = IntegerField()



def setup(Answer = "Default"):
    if Answer == "Default":
        Answer = raw_input("This function will drop all tables & content (If any exists). Do you want to continue? ")
    if Answer == 'Y' or Answer == 'y':
        print("Dropping tables...")
        db.connect()
        #SensorValues.drop_table(fail_silently=True)
        Sensors.drop_table(fail_silently=True)
        SensorTypes.drop_table(fail_silently=True)
        Plants.drop_table(fail_silently=True)
        Garden.drop_table(fail_silently=True)
        #InitialPins.drop_table(fail_silently=True)
        print("Creating Tables..")
        Garden.create_table(fail_silently=True)
        Plants.create_table(fail_silently=True)
        SensorTypes.create_table(fail_silently=True)
        Sensors.create_table(fail_silently=False)
        #SensorValues.create_table(fail_silently=True)
        #InitialPins.create_table(fail_silently=True)
    else:
        print("Abort")

if __name__ == '__main__':
    setup()
