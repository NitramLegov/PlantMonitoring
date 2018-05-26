from __future__ import print_function
import ConfigParser
import json

settings_file_name = 'Plantmonitoring.conf'
def save():
    with open(settings_file_name, 'wb') as config_file:
        configuration.write(config_file)
def defaultValues():
    #configuration = ConfigParser.SafeConfigParser()
    configuration.add_section('Server')
    configuration.set('Server','#Here, please configure your networking settings.')
    configuration.set('Server','#Use 0.0.0.0 as host to listen to all IPv4 devices.')
    configuration.set('Server','#Use :: as host to listen to all IPv4 and IPv6 devices.')
    configuration.set('Server','PORT','8080')
    configuration.set('Server','HOST','127.0.0.1')
    configuration.add_section('Initial Pins')
    configuration.set('Initial Pins','High', json.dumps([['Name1',23], ['Name2',24],['Name2',25],['Name2',8],['Name2',26]]))
    configuration.add_section('General Setup')
    configuration.set('General Setup','MCP_Relais', '0x24')
    configuration.set('General Setup','MCP_Sensor_Activation', '0x20')
    save()
#Default Values
#PIN: 23 Value: 1
#PIN: 24 Value: 1
#PIN: 25 Value: 1
#PIN: 8 Value: 1
#PIN: 26 Value: 1

configuration = ConfigParser.SafeConfigParser(allow_no_value=True)

try:
    #with open(settings_file_name,'r') as config_file:
    configuration.read(settings_file_name)
    print('Configuration loaded successfully')
except:
    defaultValues()

def setValues(newSettings):
    try:
        for section in newSettings:
            for setting in newSettings[section]:
                if configuration.has_section(section):
                    configuration.set(section,setting[0],setting[1])
                else:
                    configuration.add_section(section)
                    configuration.set(section,setting[0],setting[1])
        save()
        return 'Successfully changed the settings. Please restart the server to reload them.'
    except Exception as e:
        return e


