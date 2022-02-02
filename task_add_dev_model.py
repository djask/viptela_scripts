# CPOC PBST template add model script
from vmanage.api.feature_templates import FeatureTemplates
from vmanage.api.device_templates import DeviceTemplates
import pprint
import sys

from lib_vmanage import *

auth, vmanage_host =  get_vmanage_auth('pbst2.ini')
pp = pprint.PrettyPrinter(indent=1, width=180)
ft = FeatureTemplates(auth, vmanage_host)
vdt = DeviceTemplates(auth, vmanage_host)

tlist = ft.get_feature_template_list()


def add_device(new_dev):
    for template in tlist:
        print(template['deviceType'])
        if new_dev not in template['deviceType']:
            template['deviceType'].append(new_dev)
            pp.pprint(ft.update_feature_template(template))

def del_device(new_dev):
    for template in tlist:
        #print(template['deviceType'])
        if new_dev in template['deviceType']:
            template['deviceType'].remove(new_dev)
            pp.pprint(ft.update_feature_template(template))

new_dev = input("New device model to add to batch templates [vedge-ISR-4431]: ")
resp = add_device(new_dev)
update_affected_templates(vdt, resp)