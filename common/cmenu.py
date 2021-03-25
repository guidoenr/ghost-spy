import cginput

class Menu:
    def __init__(self, menu_text, valid_options):
        self.menu = menu_text
        self.valid_options = valid_options
        self.g_input = cginput.Ginput(valid_options)

    def show_menu(self):
        print(self.menu)

    def read_input(self):
        return self.g_input.read()

    def is_a_valid_option(self, option):
        return True if self.valid_options.__contains__(option) else False
