#!/usr/bin/env python

'''
- Allows you to send sample change to an IOS-XR device
- If changes are required these will be printed and deployed
- If no changes are required a message will be printed

'''

from napalm_base import get_network_driver
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--router_ip", help="Enter device ip address")
args = parser.parse_args()
device_ip = args.router_ip

driver = get_network_driver('iosxr')
device = driver(username='vagrant',
                password='vagrant',
                optional_args={'port':2221},
                hostname=device_ip)


device.open()
print 'Napalm Is Running........'
device.load_merge_candidate(filename='new_loopbacks.cfg')
diffs = device.compare_config()


if len(diffs) > 0:
    print(diffs)

    commit = raw_input("Type COMMIT to commit the configuration or hit ENTER to abort: ")
    if commit == 'COMMIT':
    
        try:
            device.commit_config()

    
        except Exception as inst:
            print '\nAn error occurred with the commit: '
            print type(inst)
            sys.exit(inst)
            print
    
        else:
            print 'Config committed'
    
    else:
        sys.exit('Script aborted by user')
    
else:
    print('No changes needed')
    device.discard_config()

device.close()