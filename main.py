import os
import sys

MENUU = os.getcwd() + '/menu'
CONFIGURATION = os.getcwd() + '/configuration'
COMMON = os.getcwd() + '/common'
RESOURCES = os.getcwd() + '/resources'
sys.path.append(MENUU)
sys.path.append(CONFIGURATION)
sys.path.append(COMMON)
sys.path.append(RESOURCES)

from menu import main_menu

if __name__ == '__main__':
    main_menu.show()
