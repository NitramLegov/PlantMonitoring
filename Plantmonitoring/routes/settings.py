import web
import controller.settings as settings
import json

class Settings(object):
    """description of class"""

    def GET(self,section=None,setting=None):
        if section != '' and section != None:
            if setting == None:
                return json.dumps(settings.configuration.items(section))
            else:
                return json.dumps(settings.configuration.get(section,setting))
        else:
            returnDict = {}
            for section in settings.configuration.sections():
                returnDict[section] = settings.configuration.items(section)
            return json.dumps(returnDict)

    def POST(self,section=None):
        data = json.loads(web.data())
        dictToReturn = {'message': settings.setValues(data)}
        web.header('Content-Type', 'application/json')
        return json.dumps(dictToReturn)
        

