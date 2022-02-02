#AAR toggle/change Script

from vmanage.api.authentication import Authentication
from vmanage.api.device import Device
from vmanage.api.policy_definitions import PolicyDefinitions
from vmanage.api.device_templates import DeviceTemplates
import pprint
import re

from lib_vmanage import *

auth, vmanage_host = get_vmanage_auth('pbst.ini')

#vd = Device(auth, vmanage_host)
vp = PolicyDefinitions(auth, vmanage_host)
vdt = DeviceTemplates(auth, vmanage_host)

pp = pprint.PrettyPrinter(indent=1, width=180)

def toggle_transport(t):
    if t == "mpls": return "public-internet"
    elif t == "public-internet": return "mpls"
    
    #should not get here
    return "mpls"

#check we have approute policies available
if 'approute' in vp.get_definition_types():
    print("loading all approute policies")
    aar_policies = vp.get_policy_definition_list('approute')
    
    for aarp in aar_policies:
        new_aarp = aarp
    
        #we are only modifying policies with API suffix
        if not re.match(".*_API$", aarp['name']):
            continue
        
        #check all sequences for preferred color
        print("found matching AAR to modify")
        pp.pprint(aarp['definitionId'])
        
        
        #toggle preferred color for DSCP46 packets
        for i in range(0, len(aarp['sequences'])):
            s = aarp['sequences'][i]
            #pp.pprint(s)
            for j in range(0, len(s['actions'])):
                p = s['actions'][j]
                #pp.pprint(p)
                if p['type'] == 'slaClass':
                    print ("current pref color is {}".format(p['parameter'][1]['value']))
                    new_aarp['sequences'][i]['actions'][j]['parameter'][1]['value'] = toggle_transport(p['parameter'][1]['value'])
                elif p['type'] == 'backupSlaPreferredColor':
                    print ("current backup pref color is {}".format(p['parameter']))
                    new_aarp['sequences'][i]['actions'][j]['parameter'] = toggle_transport(p['parameter'])
                    
        
        print('toggling transport on AAR policy')
        
        resp = vp.update_policy_definition(new_aarp, new_aarp['definitionId'])
        pp.pprint(resp)
        pp.pprint(update_affected_templates(vdt, resp))