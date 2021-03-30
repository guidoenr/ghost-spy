import main_menu
from common import cmenu
from configuration import configpar as cp


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
    freq = cp.config_get('frequency', 'frequency')
    return 'frequency: \33[1m{}'.format(freq) + ' minutes \33[0m'


def update_frequency(number):
    cp.config_load()
    cp.config_set('frequency', 'frequency', number)
    cp.config_save()


def show():
    freq_menu = cmenu.FreqMenu(menu_string.format(load_frequency_menu()))
    freq_menu.clean_terminal()
    freq_menu.show_menu()

    freq = freq_menu.read_input()
    while freq != 'q':
        update_frequency(freq)
        freq_menu.set_menu(menu_string.format(load_frequency_menu()))
        freq_menu.clean_terminal()
        freq_menu.show_menu()
        freq = freq_menu.rea