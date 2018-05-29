import controller.Database as Database
from controller.Database import *
import peewee
from peewee import *

def dataGenerator():
    Database.setup("Y")
    Garden1 = Garden()
    Garden1.Name = "Test Garden"
    Garden1.NumberOfColumns = 4
    Garden1.NumberOfRows = 4
    Garden1.save()
