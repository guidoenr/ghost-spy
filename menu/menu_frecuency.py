import menu_email
import menu_main
from common import tools
from configuration import configpar as cp
from resources import constant

menu = """\033[92m[frecuency_menu]\033[0m
here, you can configure how often you want ghostspy 
to take information from your computer, keep in mind 
that a fairly short period could generate spam to 
your method of receiving messages.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    [m] new frecuency minutes
    [0] back to main menu                  
"""


def load_frecuency_menu():
    cp.config_load()
    stry = cp.config_get('frecuency', 'frecuency')
    return '\33[32mfrecuency:\33[0m \33[1m{}\33[0m'.format(stry) + ' minutes'

def update_frecuency(number):
    cp.config_load()
    cp.config_set('frecuency', 'frecuency', str(number))
    cp.config_save()

def show_menu():
    tools.clean_terminal()
    print(menu.format(load_frecuency_menu()))
    option = tools.read_input()
    while not option < 120 and option >= 1:
        tools.print_bad_number()
        option = tools.read_input()
    if option == constant.const.MAIN_MENU:
        menu_main.show_menu()
    else:
        update_frecuency(option)
        show_menu()
