import email_menu
import frequency_menu
import tools_menu
import status_menu
import help_menu
from common import cmenu

menu_str = """[main_menu]\033[92m     
                             
 ___ (___  ___  ___ (___      ___  ___      
|   )|   )|   )|___ |    ___  |___ |   )\   )
|__/ |  / |__/  __/ |__        __/ |__/  \_/ 
__/                                |      / 

@author: guidoenr
@github : github.com/guidoenr/ghost-spy
@version : 1.0.0
\033[0m

options:

    \33[32m[1]\033[0m enable/disable tools
    \33[32m[2]\033[0m information delivery strategy
    \33[32m[3]\033[0m delivery frecuency
    \33[32m[4]\033[0m status
    
    \33[36m[help]\033[0m show help
    \33[36m[q]\033[0m quit
"""


def show():
    main_menu = cmenu.Menu(menu_str)
    switcher = {
        '1': tools_menu.show,
        '2': email_menu.show,
        '3': frequency_menu.show,
        '4': status_menu.show,
        'help': help_menu.show,
        'q': main_menu.quit
    }

    main_menu.set_switcher(switcher)
    main_menu.clean_terminal()

    main_menu.show_menu()
    option = main_menu.read_input()
    main_menu.switch(option)
