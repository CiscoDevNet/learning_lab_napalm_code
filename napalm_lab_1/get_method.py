'''
- Allows you to get router methods from an IOS-XR device
- python get_facts.py -ip [ip address]
'''
import json
from napalm_base import get_network_driver
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--router_ip", help="Enter device ip address")
args = parser.parse_args()
device_ip = args.router_ip

driver = get_network_driver('ios')
device = driver(username='vagrant',
                password='vagrant',
                optional_args={'port':2222},
                hostname=device_ip)

device.open()
get_method = dir(device)


# print get_method
print(json.dumps(get_method, sort_keys=True, indent=4))
# for word in get_method:
#     if word.startswith('get'):
#     	print(json.dumps(get_method, sort_keys=True, indent=4))



device.close()