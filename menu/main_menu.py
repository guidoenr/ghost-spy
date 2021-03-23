import common.bcolors as bcolors
import toolsmenu, emailmenu, frecuencymenu, os

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

valid_options = [0,1,2,3]

TOOLS = 1
EMAIL = 2
FRECUENCY = 3
QUIT = 4

def ginput():
    inp = int(input("\033[95m$ghostspy:~\033[0m "))
    return inp

def show_menu():
    print(menu)
    option = ginput()
    while not valid_options.__contains__(option):
        prynter.print_red("[ERROR]: the option doesn't exist, plase enter a valid option")
        option = ginput()
    while option != 0:
        if option == TOOLS:
            toolsmenu.show_menu()
        if option == EMAIL:
            emailmenu.show_menu()
        if option == FRECUENCY:
            frecuencymenu.show_menu()

show_menu()
