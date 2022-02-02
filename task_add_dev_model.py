# CPOC PBST template add model script
from vmanage.api.device import Device
from vmanage.api.policy_definitions import PolicyDefinitions
from vmanage.api.device_templates import DeviceTemplates
import pprint

from lib_vmanage import get_vmanage_auth

auth, vmanage_host =  get_vmanage_auth('pbst2.ini')

#vd = Device(auth, vmanage_host)
vp = PolicyDefinitions(auth, vmanage_host)
vdt = DeviceTemplates(auth, vmanage_host)

pp = pprint.PrettyPrinter(indent=1, width=180)