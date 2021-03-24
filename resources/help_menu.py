from common import tools
from menu import menu_main
from resources import constant

menu = """ghost-py was developed by @guidoenr 
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

def show_menu():
    tools.clean_terminal()
    print(menu)
    option = tools.read_input()
    if option == constant.const.MAIN_MENU:
        menu_main.show_menu()
