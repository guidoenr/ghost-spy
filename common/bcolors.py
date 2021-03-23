class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BEST = '\33[4m'
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


def print_green(text):
    print(bcolors.OKGREEN + text + bcolors.ENDC)

def print_blue(text):
    print(bcolors.OKBLUE + text + bcolors.ENDC)

def print_best(text):
    print(bcolors.CGREEN + text + bcolors.ENDC)

def print_curl(text):
    print(bcolors.CURL + text + bcolors.ENDC)

def print_warning(text):
    print(bcolors.WARNING + text + bcolors.ENDC)

def print_red(text):
    print(bcolors.FAIL + text + bcolors.ENDC)

def print_cviolet(text):
    print(bcolors.CVIOLET + text + bcolors.ENDC)