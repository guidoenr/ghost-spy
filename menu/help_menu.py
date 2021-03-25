from common import cprinter, cmenu
from menu import main_menu
from resources import constant


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

[0] back to main menu

"""

def show():
    pr = cprinter.Printer()
    helpMenu = cmenu.Menu(menu_string, [0])

    pr.clean_terminal()
    helpMenu.show_menu()

    option = helpMenu.read_input()

    while not helpMenu.is_a_valid_option(option):
        pr.warning('Press 0 to back to the main menu')
        option = helpMenu.read_input()
    if option == constant.MAIN_MENU:
        main_menu.show()
