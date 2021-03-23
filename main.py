import sys, os

MENU = '/menu'
CONFIGURATION = '/configuration'
COMMON = '/common'
RESOURCES = '/resources'

def get_py_path(folder):
    return os.getcwd() + folder

def append_wd_to_path():
    sys.path.append(get_py_path(MENU))
    sys.path.append(get_py_path(CONFIGURATION))
    sys.path.append(get_py_path(COMMON))
    sys.path.append(get_py_path(RESOURCES))

append_wd_to_path()
from menu import menu_main

if __name__ == '__main__':
    mainMenu = menu_main.mainMenu
    mainMenu.show_menu()
