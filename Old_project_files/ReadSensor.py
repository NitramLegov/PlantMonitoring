__author__ = 'Martin'
import time
import spidev
import RPi.GPIO as GPIO
import SensorHelperClass as Helper
import Adafruit_DHT
from Adafruit_DHT import *


GPIO.setmode(GPIO.BCM)
spi = spidev.SpiDev()

def readDHT11TemperatureSensor (Pin):
    return Adafruit_DHT.common.read(DHT11,Pin)


def readSoilMoistureSensor (enablePin, SPI_CHIP,CHIP_SELECT,Channel):
    if enablePin != 0:
        GPIO.setup(enablePin,GPIO.OUT)
        GPIO.output(enablePin,GPIO.HIGH) #Enable the Soil Moisture Sensor
        time.sleep(2)
    spi.open(SPI_CHIP,CHIP_SELECT)
    Results = []
    for i in xrange(20):
        Results.append(Helper.MCP3008_readAdc(spi, Channel))
        time.sleep(0.2)

    time.sleep(0.2)
    Helper.MCP3008_readAdc(spi, Channel)
    time.sleep(0.2)
    Helper.MCP3008_readAdc(spi, Channel)
    if enablePin != 0:
        GPIO.cleanup()
    spi.close()
    Results.sort()
    return Results


def TestSensors():
    #Dry Sensor
    TestChannel = 0
    TestPin = 4
    #Test = [1,2,3,4,5,6,7,8,9,0]
    Test = readSoilMoistureSensor(TestPin,0,0,TestChannel)
    Average = 0
    for value in Test:
        Average = Average + value
    Average = Average / len(Test)

    print 'Channel ' + str(TestChannel) + ": " + str(Test) + str(Test[9]) + ' ' + str(Test[19] - Test[0]) + ' ' + str(Average)

    #middle Sensor
    TestChannel = 1
    TestPin = 17
    Test = readSoilMoistureSensor(TestPin,0,0,TestChannel)
    Average = 0
    for value in Test:
        Average = Average + value
    Average = Average / len(Test)

    print 'Channel ' + str(TestChannel) + ": " + str(Test) + str(Test[9]) + ' ' + str(Test[19] - Test[0]) + ' ' + str(Average)

    #Wet Sensor
    TestChannel = 2
    TestPin = 27
    Test = readSoilMoistureSensor(TestPin,0,0,TestChannel)
    Average = 0
    for value in Test:
        Average = Average + value
    Average = Average / len(Test)

    print 'Channel ' + str(TestChannel) + ": " + str(Test) + str(Test[9]) + ' ' + str(Test[19] - Test[0]) + ' ' + str(Average)

    #Poti
    TestChannel = 7
    TestPin = 0
    Test = readSoilMoistureSensor(TestPin,0,0,TestChannel)
    Average = 0
    for value in Test:
        Average = Average + value
    Average = Average / len(Test)

    print 'Channel ' + str(TestChannel) + ": " + str(Test) + str(Test[9]) + ' ' + str(Test[19] - Test[0]) + ' ' + str(Average)

    #DHT11
    values = readDHT11TemperatureSensor(21)
    if values[1] == None:
        print "Error while reading Temperature"
    else:
        print 'Temperature: ' + str(values[1])
        print 'Humidity ' + str(values[0])

if __name__ == '__main__':
    TestSensors()