#!/usr/bin/env python

##############################################################
# Learning Module: Introducation to Napalm
# Author: Stuart Clark <stuaclar@cisco.com>
#
#
# Allows you to get router ports and errors from an IOS-XR device
# python get_ports_pretty -ip [ip address]
##############################################################


from napalm_base import get_network_driver
from prettytable import PrettyTable
from datetime import datetime
import argparse



Interface_Errors = PrettyTable(['Interface', 'RX Errors', 'Tx Errors', "MAC Address", "Port Up"])
Interface_Errors.padding_width = 1

Interface_Discards = PrettyTable(['Interface', 'RX Discards', 'Tx Discards', "MAC Address","Port Up"])
Interface_Discards.padding_width = 1

parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--router_ip", help="Enter device ip address")
args = parser.parse_args()
device_ip = args.router_ip

driver = get_network_driver('iosxr')
device = driver(username='cisco',
                password='cisco',
                hostname=device_ip)


device.open()
print 'Napalm Is Running........'

interfaces_counters = device.get_interfaces_counters()
interfaces = device.get_interfaces()


for int, int_data in sorted(interfaces_counters.iteritems()):
	Interface_Errors.add_row([int, int_data["rx_errors"], int_data["tx_errors"],interfaces[int]["mac_address"],interfaces[int]["is_up"]])
	Interface_Discards.add_row([int, int_data["rx_discards"], int_data["tx_discards"],interfaces[int]["mac_address"],interfaces[int]["is_up"]])

	if int_data["rx_errors"] > 0 or \
	   int_data["tx_errors"] > 0 or \
	   int_data["rx_discards"] > 0 or \
	   int_data["tx_discards"] > 0:
	   print "interface {} has errors" .format(int)

print "=" * 60
print Interface_Errors 
print "=" * 60
print Interface_Discards 
print str(datetime.now()) + " Gathered information from {}" .format(device_ip)