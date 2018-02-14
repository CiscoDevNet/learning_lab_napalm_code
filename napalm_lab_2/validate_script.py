#!/usr/bin/python
#
#
from napalm_base import get_network_driver
from pprint import pprint
from datetime import datetime
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


print str(datetime.now()) + " Gathering Information from {}" .format(device_ip)
pprint(device.compliance_report("validate-iosxr.yml"))