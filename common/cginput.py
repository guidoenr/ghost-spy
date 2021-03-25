import cprinter

class Ginput:
    def __init__(self, valid_options):
        self.valid_options = valid_options
        self.printer = cprinter.Printer()

    def read(self):
        inp = -1
        try:
            inp = int(input("\033[95m$ghostspy:~\033[0m "))
            return inp
        except ValueError:
            self.printer.error('Not a valid input')

