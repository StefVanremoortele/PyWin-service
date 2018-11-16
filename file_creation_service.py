import time
import os
import random
from pathlib import Path
from SMWinservice_base import SMWinservice

class File_creation_service(SMWinservice):
    _svc_name_ = "PyWinService"
    _svc_display_name_ = "pywin-file-creator" 
    _svc_description_ = "use if you want to annoy some1"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:
            random.seed()
            x = random.randint(1, 1000000)
            user = os.environ['USERNAME']
            os.system("python C:\\users\clydez\Desktop\python-windows-service\\file_creator.py")
            time.sleep(5)

if __name__ == '__main__':
    File_creation_service.parse_command_line()