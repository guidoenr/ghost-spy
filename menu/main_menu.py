import email_menu
import frequency_menu
import tools_menu
from common import cmenu, cprinter
from resources import constant
from menu import help_menu

menu_string = """[main_menu]\033[92m     
                             
 ___ (___  ___  ___ (___      ___  ___      
|   )|   )|   )|___ |    ___  |___ |   )\   )
|__/ |  / |__/  __/ |__        __/ |__/  \_/ 
__/                                |      / 

@author: guidoenr
@github : github.com/guidoenr/ghost-spy
@version : 1.0.0
\033[0m
---------------------------------------
options:
    \33[32m[1]\033[0m enable/disable tools
    \33[32m[2]\033[0m information delivery strategy
    \33[32m[3]\033[0m ghost-spy frecuency
    
    \33[32m[4]\033[0m show help
    \33[32m[0]\033[0m quit
"""


def show():
    pr = cprinter.Printer()
    mainMenu = cmenu.Menu(menu_string, [0, 1, 2, 3, 4])

    pr.clean_terminal()
    mainMenu.show_menu()
    option = mainMenu.read_input()

    while not mainMenu.is_a_valid_option(option):
        pr.error('That option is invalid, please select one in range {}'.format(str(mainMenu.valid_options)))
        option = mainMenu.read_input()

    if option == constant.QUIT:
        exit()
    if option == constant.TOOLS:
        tools_menu.show()
    if option == constant.EMAIL:
        email_menu.show_menu()
    if option == constant.FRECUENCY:
        frequency_menu.show()
    if option == constant.HELP:
        help_menu.show()
