import configparser, resources.paths as paths

config = configparser.ConfigParser()
configpath = paths.CONFIG_PATH

def config_load():
    config.read(configpath)


def config_get(section, key):
    return config.get(section, key)


def config_save():
    with open(configpath, 'w') as configfile:
        config.write(configfile)

def config_switch_key(section, key):
    config.set(section, key, str(not config.get(section, key)))
    config_save()

def config_get_boolean(section, key):
    return config[section].getboolean(key)