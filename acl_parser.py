#!/usr/bin/env python3
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help = "input file containing access-lists and object-groups")
args = parser.parse_args()
in_file = args.file

re_acl_name = re.compile("ip access-list extended (?P<acl_name>\S+)$")
re_service_group_name = re.compile("object-group service (?P<service_group_name>\S+)")
re_network_group_name = re.compile("object-group network (?P<network_group_name>\S+)")
re_net_obj = re.compile("\s*(?P<host>host)?\s*?(?P<net_address>(\d+\.){3}\d+)\s*(?P<net_mask>(\d+\.){3}\d+)?")

if not in_file:
    exit("please specify a path to the file containing access-lists and object-groups..")

acls = {}
service_groups = {}
network_groups = {}
level = ""

with open(in_file) as INPUT_FILE:
    for line in INPUT_FILE:
        if re_acl_name.match(line):
            acl_name = re_acl_name.match(line).group("acl_name") 
            print("acl name: %s" % acl_name)
            acls[acl_name] = {}
            level = "acl"
        elif re_service_group_name.match(line):
            service_group_name = re_service_group_name.match(line).group("service_group_name")
            print("service object-group: %s" % service_group_name)
            service_groups[service_group_name] = [] 
            level = "service_group"
        elif re_network_group_name.match(line):
            network_group_name = re_network_group_name.match(line).group("network_group_name")
            print("network object-group: %s" % network_group_name)
            network_groups[network_group_name] = [] 
            level = "network_group"
        elif level == 'network_group':
            if re_net_obj.match(line):
                network_groups[network_group_name].append(re_net_obj.match(line).group("net_address"))

print(acls)
print(service_groups)
print(network_groups)
