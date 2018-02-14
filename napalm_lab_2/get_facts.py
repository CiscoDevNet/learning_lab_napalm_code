#!/usr/bin/env python

'''
- Allows you to get router facts change to an IOS-XR device

'''

from napalm_base import get_network_driver


driver = get_network_driver('iosxr')
device = driver(hostname='10.4.37.16', username='cisco',
             password='cisco')

device.open()
router_dic = device.get_facts()


for i in router_dic:
   if type(router_dic[i]) == list:
     for k in router_dic[i]:
       print "\t -{}".format(k)
   else:
     print "{}: {}".format(i, router_dic[i])


device.close()



