import menu_email
import menu_tools
import menu_frecuency
from common import tools
from resources import constant, help_menu

menu = """\033[92m[main_menu]     
                             
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
    [1] enable/disable tools
    [2] configure email
    [3] spy frecuency
    
    [4] show help
    [0] quit
"""

valid_options = [0, 1, 2, 3, 4]

def show_menu():
    tools.clean_terminal()
    print(menu)
    option = tools.read_input()
    while not valid_options.__contains__(option):
        tools.print_error()
        option = tools.read_input()
    if option == constant.const.QUIT:
        exit()
    if option == constant.const.TOOLS:
        menu_tools.show_menu()
    if option == constant.const.EMAIL:
        menu_email.show_menu()
    if option == constant.const.FRECUENCY:
        menu_frecuency.show_menu()
    if option == constant.const.HELP:
        help_menu.show_menu()
