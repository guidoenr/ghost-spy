from common import cmenu, cprinter
from resources import constant

menu_string = """\33[92m
                  WELCOME TO 
                  
 ___ (___  ___  ___ (___      ___  ___      
|   )|   )|   )|___ |    ___  |___ |   )\   )
|__/ |  / |__/  __/ |__        __/ |__/  \_/ 
__/                                |      / 
\033[0m
If you have already read the documentation, you will know 
that this script works at the cost of a telegram BOT to be 
configurable from your cell phone.
Be sure to have telegram installed on your cell phone.
If you already have it installed, you just need to create a 
username and password for this computer! so you can connect 
from telegram as well.



"""


def show():
    pr = cprinter.Printer()
    loginMenu = cmenu.Menu(menu_string, [])

    pr.clean_terminal()
    loginMenu.show_menu()
    option = loginMenu.read_input()
