import web
import controller.settings as settings
import temp.TestDataGenerator
import json
import tempfile

class Testdata(object):
    """description of class"""

    def GET(self):
        temp.TestDataGenerator.dataGenerator()
        return 'Data Generated'


