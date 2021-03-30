from common import cprinter, cmenu
from menu import main_menu
from resources import constants


menu_string = """ghost-py was developed by @guidoenr 
its a simple script that allows to the computers owners
to get some sensitive information about who is using the
pc, a kind of 'malware' but a good one.
\33[5m
\33[34m
 ___ (___  ___  ___ (___      ___  ___      
|   )|   )|   )|___ |    ___  |___ |   )\   )
|__/ |  / |__/  __/ |__        __/ |__/  \_/ 
__/                                |      / 
\33[0m
\33[0m
version: 1.1.0
mark: 1

[q] back to main menu

"""


def show():
    help_menu = cmenu.Menu(menu_string)

    help_menu.clean_terminal()
    help_menu.show_menu()
    switcher = {
        'q': main_menu.show
    }
    help_menu.set_switcher(switcher)
    option = help_menu.read_input()
    help_menu.switch(option)