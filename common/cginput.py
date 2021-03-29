import cprinter

class Ginput:
    def __init__(self):
        self.printer = cprinter.Printer()

    def read_option(self):
        try:
            inp = int(input("\33[92mghost@spy:~$\033[0m "))
            return inp
        except ValueError:
            self.printer.error('Not a valid input')
