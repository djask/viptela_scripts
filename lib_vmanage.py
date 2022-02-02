import getpass
import configparser

from vmanage.api.authentication import Authentication

def get_vmanage_auth(config_file):
    config = configparser.ConfigParser()
    config.sections()

    config.read(config_file)

    vmanage_host = config['vmanage']['host']
    vmanage_username = config['vmanage']['username']
    if 'password' in config['vmanage']:
        vmanage_password = config['vmanage']['password']
    else:
        vmanage_password = getpass.getpass()

    auth = Authentication(host=vmanage_host, user=vmanage_username,
                                password=vmanage_password).login()
    return auth, vmanage_host
