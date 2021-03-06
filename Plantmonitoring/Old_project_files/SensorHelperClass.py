__author__ = 'Martin'

import time
import spidev

spi = spidev.SpiDev()




def MCP3008_buildReadCommand(channel):
    startBit = 0x01
    singleEnded = 0x08

    return [startBit, singleEnded|(channel<<4), 0]

def MCP3008_processAdcValue(result):
    '''Take in result as array of three bytes.
       Return the two lowest bits of the 2nd byte and
       all of the third byte'''
    byte2 = (result[1] & 0x03)
    return (byte2 << 8) | result[2]


def MCP3008_readAdc(spi,channel):
    if ((channel > 7) or (channel < 0)):
        return -1
    r = spi.xfer2(MCP3008_buildReadCommand(channel))
    return MCP3008_processAdcValue(r)
