import os, datetime
route = os.path.abspath(__file__)[:-8]


def generate_day_folder(today):
    os.mkdir(route + str(today), 0o666)
