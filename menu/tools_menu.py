from configuration import configpar as cp
from common import cprinter, cmenu
import main_menu
from resources import constant
from common import cginput

menu_string = """\033[92m[tools_menu]\033[0m
modules running:
~~~~~~~~~~~~~~~~~~~~~~~~~~
{}~~~~~~~~~~~~~~~~~~~~~~~~~~

[0] back to main menu

"""

def load_tools_values():
    cp.config_load()
    strings = ''
    i = 1
    for tool_key in cp.config['tools']:
        strings = strings + format_tool(tool_key, '[{}] '.format(i)) + ' \n'
        i += 1
    return strings

def format_tool(tool_key, num):
    status = cp.config_get('tools', tool_key)
    stry = r'{}: '.format(tool_key)
    if status == 'enabled':
        return num + stry + '\033[92m enabled \033[0m'
    else:
        return num + stry + '\033[91m disabled \033[0m'



def show():
    pr = cprinter.Printer()
    updated = load_tools_values()
    toolsMenu = cmenu.Menu(menu_string.format(load_tools_values()), [0, 1, 2, 3, 4, 5])

    pr.clean_terminal()
    toolsMenu.show_menu()
    option = toolsMenu.read_input()


    while not toolsMenu.is_a_valid_option(option):
        pr.error("That module doesn't exist")
        option = toolsMenu.read_input()
    while option != 0:
        if option == constant.GEOLOCATION:
            cp.config_switch_key('tools', 'geolocator')
            show()
        if option == constant.KEYLOGGER:
            cp.config_switch_key('tools', 'keylogger')
            show()
        if option == constant.SCREENSHOT:
            cp.config_switch_key('tools', 'screenshot')
            show()
        if option == constant.SYSTEMINFO:
            cp.config_switch_key('tools', 'systeminfo')
            show()
        if option == constant.WEBCAM:
            cp.config_switch_key('tools', 'webcam')
            show()
    if option == constant.MAIN_MENU:
        main_menu.show()
        exit()

