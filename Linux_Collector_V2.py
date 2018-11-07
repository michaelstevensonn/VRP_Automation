#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from getpass import getpass
import json
import os
import sys
import time

# Define the log file name format
timestr = time.strftime("%Y%m%d_%H%M%S")
outputfile = timestr + '-output.log'

# Define the login info
device = {
    'device_type': 'linux',
    'host': '192.168.1.1',
    'username': 'Michael',
    'password': 'password',
} 

# Connect to device using the parameters above
net_connect = ConnectHandler(**device)

# Open the log file
log = open(outputfile,'a')

# Read the pre-defined commmand list from file
# and loop to the last line
# pass to the send_command method as arg
commands = open('commands.txt')
for line in commands:
    output = net_connect.send_command(line, strip_command=False)
    print(output, file=log) 
    print("*"*64, file=log) 
    print(" ", file=log)
commands.close()

# print the file end notice
print("\n"*3, file=log)
print("#"*42, file=log)
print("###!ThIS IS THE END OF DATA COLLECTION!###", file=log)
print("#"*42, file=log)
