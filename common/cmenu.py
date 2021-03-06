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


class FreqMenu(Menu):

    def load_frequency_menu(self, config):
        config.config_load()
        freq = config.config_get('frequency', 'frequency')
        self.set_menu(self.menu.format('frequency: \33[1m{}'.format(freq) + ' minutes \33[0m'))

    @staticmethod
    def update_frequency(number, config):
        config.config_load()
        config.config_set('frequency', 'frequency', str(number))
        config.config_save()

    def switch(self, option):
        try:
            int(option)
        except ValueError:
            self.printer.error('Frequency must be a integer')
            new_option = self.read_input()
            self.switch(new_option)
