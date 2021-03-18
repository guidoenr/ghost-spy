import configparser, os

config = configparser.ConfigParser()

def create_config():
    if not os.path.isfile('config.ini'):
        config['DEFAULT'] = {
            'webcam': True,
            'systeminfo': False,
            'keylogger': True,
            'screenshot': False
        }
        config['Intervals'] = {
            'email_send' : 10,
            'screenshot' : 10,
            'webcam' : 10
        }
        config['Account'] = {
            'sender': 'sender@gmail.com',
            'password': 'password'
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    else:
        config.read('config.ini')

def set(section, key, value):
    config.set(section, key, value)

def get(key):
    return config.get('DEFAULT',key)

create_config()


