import os

class System(object):
    """description of class"""
    def GET(self,function=None):
        if function == 'shutdown':
            os.system ('sudo shutdown --poweroff now')
        elif function =='reboot':
            os.system ('sudo reboot now')
        elif function =='restartServer':
            os.system ('sudo systemctl restart Plantmonitoring.service')
        else:
            return 'please use this API with /shutdown, /reboot or /restartServer'
        

