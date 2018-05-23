#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help = "input file containing access-lists and object-groups")
args = parser.parse_args()
in_file = args.file

print("input file is %s"  % in_file)
