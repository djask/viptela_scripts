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

def update_affected_templates(vdt, resp):
    vsmart_tids = resp['json']['masterTemplatesAffected']

    #update the vsmart template from affected templates above
    print ('got vsmart template id')
    print(vsmart_tids)

    print ('updating vsmart template, please wait...')
    return vdt.reattach_multi_device_templates(vsmart_tids)
