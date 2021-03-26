import os, datetime
route = os.path.abspath(__file__)[:-8]


def generate_day_folder():
    path = route + str(datetime.datetime.today().date())
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path, 0o666)
    return path


def generate_today_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")