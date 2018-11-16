import time
import os
import random
from pathlib import Path


class File_creator():
    def exhaust_desktop(self):
        random.seed()
        x = random.randint(1, 1000000)
        user = os.environ['USERNAME']
        Path(f'c:\\users\{user}\Desktop\{x}.txt').touch()


if __name__ == '__main__':
    fc = File_creator()
    fc.exhaust_desktop()