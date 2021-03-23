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
    case = ''
    if config.get(section, key) == 'enabled':
        case = 'disabled'
    else:
        case = 'enabled'
    config.set(section, key, case)
    config_save()
    config_load()

def config_get_boolean(section, key):
    return config[section].getboolean(key)