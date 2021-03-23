import sys, os

MENU = os.getcwd() + '/menu'
CONFIGURATION = os.getcwd() +  '/configuration'
COMMON = os.getcwd() + '/common'
RESOURCES = os.getcwd() +  '/resources'

def append_wd_to_path():
    sys.path.append(MENU)
    sys.path.append(CONFIGURATION)
    sys.path.append(COMMON)
    sys.path.append(RESOURCES)


append_wd_to_path()
from menu import menu_main

if __name__ == '__main__':
    menu_main.show_menu()
