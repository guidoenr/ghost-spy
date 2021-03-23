from configuration import configpar as cp
from common import tools
import menu_main

def load_tools_values():
    cp.config_load()
    strings = ''
    for tool_key in cp.config['tools']:
        strings = strings + format_tool(tool_key) + ' \n'
    return strings

def format_tool(tool_key):
    status = (cp.config_get_boolean('tools', tool_key))
    stry = r'{}: '.format(tool_key)
    if status:
        return stry + '\033[92m enabled \033[0m'
    else:
        return stry + '\033[91m disabled \033[0m'

tls = load_tools_values()
menu = """
\033[93m
these are the current options in your configuration, choose one to deactivate or activate:
\033[0m

{}

    [0] back to main menu

""".format(tls)

valid_options = [0, 1, 2, 3, 4, 5]
MAIN_MENU = 0
GEOLOCATION = 1
KEYLOGGER = 2
SCREENSHOT = 3
SYSTEMINFO = 4
WEBCAM = 5

def show_menu():
    print(menu)
    option = tools.read_input()
    while not valid_options.__contains__(option):
        tools.print_error()
        option = tools.read_input()
    while option != 0:
        if option == GEOLOCATION:
            cp.config_switch_key('tools', 'geolocation')
            show_menu()
        if option == KEYLOGGER:
            cp.config_switch_key('tools', 'keylogger')
            show_menu()
        if option == SCREENSHOT:
            cp.config_switch_key('tools', 'screenshot')
            show_menu()
        if option == SYSTEMINFO:
            cp.config_switch_key('tools', 'systeminfo')
            show_menu()
        if option == WEBCAM:
            cp.config_switch_key('tools', 'webcam')
            show_menu()
        if option == MAIN_MENU:
            break
            exit()
    menu_main.show_menu()
