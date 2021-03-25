import os
from resources import constant


class Printer:

    def clean_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def format(self, text):
        print(text + constant.ENDC)

    def warning(self, text):
        self.format(constant.WARNING + "[WARNING]: " + text)

    def error(self, text):
        self.format(constant.FAIL + "[ERROR]: " + text)

    def info(self, text):
        self.format(constant.OKBLUE + "[INFO]: " + text)