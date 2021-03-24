from configuration import configpar as cp
from common import tools
import menu_main
from resources import constant

menu ="""\033[92m[tools_menu]\033[0m
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
        i+=1
    return strings

def format_tool(tool_key, num):
    status = cp.config_get('tools', tool_key)
    stry = r'{}: '.format(tool_key)
    if status == 'enabled':
        return num + stry + '\033[92m enabled \033[0m'
    else:
        return num + stry + '\033[91m disabled \033[0m'


valid_options = [0, 1, 2, 3, 4, 5]


def show_menu():
    tools.clean_terminal()
    updated = load_tools_values()
    print(menu.format(updated))
    option = tools.read_input()
    while not valid_options.__contains__(option):
        tools.print_error()
        option = tools.read_input()
    while option != 0:
        if option == constant.const.GEOLOCATION:
            cp.config_switch_key('tools', 'geolocation')
            show_menu()
        if option == constant.const.KEYLOGGER:
            cp.config_switch_key('tools', 'keylogger')
            show_menu()
        if option == constant.const.SCREENSHOT:
            cp.config_switch_key('tools', 'screenshot')
            show_menu()
        if option == constant.const.SYSTEMINFO:
            cp.config_switch_key('tools', 'systeminfo')
            show_menu()
        if option == constant.const.WEBCAM:
            cp.config_switch_key('tools', 'webcam')
            show_menu()
        if option == constant.const.MAIN_MENU:
            break
            exit()
    menu_main.show_menu()
