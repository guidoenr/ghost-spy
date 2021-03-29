import cprinter


class Menu:
    switcher = {}

    def __init__(self, menu_str):
        self.menu = menu_str
        self.printer = cprinter.Printer()

    def set_switcher(self, switcher):
        self.switcher = switcher

    def set_menu(self, menu_str):
        self.menu = menu_str

    def switch(self, option):
        while not self.switcher.get(option):
            self.printer.error('Invalid input, choose one on the menu')
            option = self.read_input()
        func = self.switcher.get(option)
        return func()

    def show_menu(self):
        print(self.menu)


    def read_input(self):
        return input("\33[92mghost@spy:~$\033[0m ")

    def clean_terminal(self):
        self.printer.clean_terminal()

    @staticmethod
    def quit():
        print('\33[36mghost@spy:~$\033[0m \33[6mgoodbye, boss\033[0m')
        exit()
