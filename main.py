import os
import sys

MENU = os.getcwd() + '/menu'
CONFIGURATION = os.getcwd() + '/configuration'
COMMON = os.getcwd() + '/common'
RESOURCES = os.getcwd() + '/resources'
MODULES = os.getcwd() + '/modules'

sys.path.append(MENU)
sys.path.append(CONFIGURATION)
sys.path.append(COMMON)
sys.path.append(RESOURCES)
sys.path.append(MODULES)

from menu import main_menu

if __name__ == '__main__':
    main_menu.show()
