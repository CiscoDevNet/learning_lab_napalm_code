#!/usr/bin/python



from napalm_base import get_network_driver
from prettytable import PrettyTable
from datetime import datetime
import argparse



bgp_peering = PrettyTable(['Remote IP', 'Description', 'Remote ASN', 'Received Prefix', 'Sent Prefix', 'Up Time' ] )
bgp_peering.padding_width = 1


parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--router_ip", help="Enter device ip address")
args = parser.parse_args()
device_ip = args.router_ip

driver = get_network_driver('iosxr')
device = driver(username='cisco',
                password='cisco',
                hostname=device_ip)

# driver = get_network_driver('iosxr')
# device = driver(hostname='10.4.37.15', username='cisco',
#              password='cisco')
device.open()

bgp_neighbors = device.get_bgp_neighbors()
bgp_neighbors = bgp_neighbors['global']['peers']
# print(bgp_neighbors.keys())

for ip, bgp_neighbors in sorted(bgp_neighbors.iteritems()):
	# print sorted(bgp_neighbors.iteritems())
	bgp_peering.add_row([ip, bgp_neighbors['description'], bgp_neighbors['remote_as'],
		bgp_neighbors['address_family']['ipv4']['received_prefixes'], 
		bgp_neighbors['address_family']['ipv4']['sent_prefixes'], bgp_neighbors['uptime']])

	if bgp_neighbors['address_family']['ipv4']['received_prefixes'] < 1:
	   print "bgp peer {} has received no prefix" .format(ip)
	if bgp_neighbors['address_family']['ipv4']['sent_prefixes'] < 1:
	   print "bgp peer {} has received sent no prefix" .format(ip)

# uptime_seconds = float(f.readline().split()[0])
# uptime_string = str(timedelta(seconds = uptime_seconds))

print "=" * 60
print bgp_peering
print str(datetime.now()) + " Gathered information from {}" .format(device_ip) 
