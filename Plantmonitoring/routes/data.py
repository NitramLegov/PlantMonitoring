import web
import controller.settings as settings
import controller.Database
import json
from playhouse.shortcuts import model_to_dict, dict_to_model
from playhouse.csv_loader import dump_csv

class Data(object):
    """description of class"""

    def GET(self,datatype=None):
        if datatype == 'Garden':
            AllValues = controller.Database.Garden.select()
        elif datatype == 'Plants':
            AllValues = controller.Database.Plants.select()
        else:
            return 'Plase use this api with /Garden'
        DictArray = []
        for SingleValue in AllValues:
            DictArray.append(model_to_dict(SingleValue))
        Output = json.dumps(DictArray)
        return Output

    def POST(self):
        #Handles CREATE
        DictArray = json.loads(web.data())
        if datatype == 'Garden':
            DataToInsert = dict_to_model(controller.Database.Garden, DictArray)
        elif datatype == 'Plants':
            DataToInsert = dict_to_model(controller.Database.Plants, DictArray)
        else:
            return 'Plase use this api with /Garden'
        DataToInsert.save()
        return 'Data posted'

