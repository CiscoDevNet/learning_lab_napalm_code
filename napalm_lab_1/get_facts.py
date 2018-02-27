#!/usr/bin/env python

'''
- Allows you to get router facts change to an IOS-XR device
- python get_facts.py -ip [ip address]
'''

from napalm_base import get_network_driver
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--router_ip", help="Enter device ip address")
args = parser.parse_args()
device_ip = args.router_ip

driver = get_network_driver('iosxr')
device = driver(username='cisco',
                password='cisco',
                hostname=device_ip)

device.open()
router_dic = device.get_facts()

# print router_dic

for i in router_dic:
   if type(router_dic[i]) == list:
     for k in router_dic[i]:
       print "\t -{}".format(k)
   else:
     print "{}: {}".format(i, router_dic[i])


device.close()


