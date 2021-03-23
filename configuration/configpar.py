import configparser, resources.paths as paths

config = configparser.ConfigParser()
configpath = paths.CONFIG_PATH

def config_load():
    config.read(configpath)


def config_set(section, key, value):
    config.set(section, key, value)


def config_get(section, key):
    return config.get(section, key)


def config_save():
    with open(configpath, 'w') as configfile:
        config.write(configfile)
