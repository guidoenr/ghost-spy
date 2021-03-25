import main_menu
from common import cprinter
from common import cmenu
from configuration import configpar as cp
from resources import constant

menu_string = """\033[92m[frequency_menu]\033[0m
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


def load_frequency_menu():
    cp.config_load()
    stry = cp.config_get('frequency', 'frequency')
    return 'frecuency: \33[1m{}'.format(stry) + ' minutes \33[0m'

def update_frequency(number):
    cp.config_load()
    cp.config_set('frequency', 'frequency', str(number))
    cp.config_save()

def show():
    frequencyMenu = cmenu.Menu(menu_string.format(load_frequency_menu()), list(range(0, 120)))
    pr = cprinter.Printer()

    pr.clean_terminal()
    frequencyMenu.show_menu()

    option = frequencyMenu.read_input()
    while not frequencyMenu.valid_options.__contains__(option):
        pr.error('Input must be a number in the range 0 - 120 (minutes)')
        option = frequencyMenu.read_input()
    if option == constant.MAIN_MENU:
        main_menu.show()
    else:
        update_frequency(option)
        show()
