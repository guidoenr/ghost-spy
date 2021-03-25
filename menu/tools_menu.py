from configuration import configpar as cp
from common import cprinter
import main_menu
from resources import constant
from common import cginput

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



def show():
    pr = cprinter.Printer()
    updated = load_tools_values()
    gInput = cginput.Ginput([0, 1, 2, 3, 4, 5])

    pr.clean_terminal()
    print(menu.format(updated))

    option = gInput.read()

    while not gInput.valid_options.__contains__(option):
        pr.error("That module doesn't exist")
        option = gInput.read()
    while option != 0:
        if option == constant.GEOLOCATION:
            cp.config_switch_key('tools', 'geolocation')
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
            break
    main_menu.show()
