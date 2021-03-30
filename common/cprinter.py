import os
from resources import constants


class Printer:

    def clean_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def format(self, text):
        print(text + constants.ENDC)

    def warning(self, text):
        self.format(constants.WARNING + "[WARNING]: " + text)

    def error(self, text):
        self.format(constants.FAIL + "[ERROR]: " + text)

    def info(self, text):
        self.format(constants.OKBLUE + "[INFO]: " + text)