#!/usr/bin/env python

##############################################################
# Learning Module: Introducation to Napalm
# Author: Stuart Clark <stuaclar@cisco.com>
#
#
# Allows you to validate configuration/settigs from an IOS-XR device
# python get_facts.py -ip [ip address]
##############################################################


from napalm_base import get_network_driver
from pprint import pprint
from datetime import datetime
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
print 'Napalm Is Running........'


print str(datetime.now()) + " Gathering Information from {}" .format(device_ip)
pprint(device.compliance_report("validate_xe.yml"))