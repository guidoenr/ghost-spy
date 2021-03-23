import bcolors as bc

def read_input():
    inp = int(input("\033[95m$ghostspy:~\033[0m "))
    return inp

def print_error():
    bc.print_red("[ERROR]: the option doesn't exist, plase enter a valid option")


