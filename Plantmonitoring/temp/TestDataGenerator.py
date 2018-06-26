import controller.Database
import controller.Database as Database
from controller.Database import *
import peewee
from peewee import *

def dataGenerator():
    controller.Database.setup("Y")
    #Database.setup("Y")
    Garden1 = Garden()
    Garden1.Name = "Test Garden"
    Garden1.NumberOfColumns = 4
    Garden1.NumberOfRows = 4
    Garden1.save()
    Plant1 = Plants()
    Plant1.Name = "Timo Thyme"
    Plant1.Location_Row = 1
    Plant1.Location_Column = 1
    Plant1.WateringLogic = 'Time'
    Plant1.WateringTreshold = 21600
    Plant1.WateringSeconds = 30
    Plant1.Garden = Garden1.ID
    Plant1.save()
    Plant1 = Plants()
    Plant1.Name = "Tom Tomato"
    Plant1.Location_Row = 2
    Plant1.Location_Column = 2
    Plant1.WateringLogic = 'Time'
    Plant1.WateringTreshold = 21600
    Plant1.WateringSeconds = 30
    Plant1.Garden = Garden1.ID
    Plant1.save()
    Plant1 = Plants()
    Plant1.Name = "Chilja Chili"
    Plant1.Location_Row = 3
    Plant1.Location_Column = 3
    Plant1.WateringLogic = 'Time'
    Plant1.WateringTreshold = 21600
    Plant1.WateringSeconds = 30
    Plant1.Garden = Garden1.ID
    Plant1.save()
    Plant1 = Plants()
    Plant1.Name = "Sally Strawberry"
    Plant1.Location_Row = 4
    Plant1.Location_Column = 4
    Plant1.WateringLogic = 'Time'
    Plant1.WateringTreshold = 21600
    Plant1.WateringSeconds = 30
    Plant1.Garden = Garden1.ID
    Plant1.save()
