import menu_email
import menu_tools
from common import tools

menu = """
\033[92m                                  
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

    [0] quit
"""

valid_options = [0, 1, 2, 3]
TOOLS = 1
EMAIL = 2
FRECUENCY = 3
QUIT = 0


def show_menu():
    print(menu)
    option = tools.read_input()
    while not valid_options.__contains__(option):
        tools.print_error()
        option = tools()
    if option == QUIT:
        exit()
    if option == TOOLS:
        menu_tools.show_menu()
