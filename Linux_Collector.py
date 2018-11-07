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
    'host': '192.168.1.177',
    'username': 'Michael',
    'password': '65831120341Myt',
} 

# Connect to device using the parameters above
net_connect = ConnectHandler(**device)

# Read the pre-defined commmand list from file
# and loop to the last line
# pass to the send_command method as arg
commands = open('commands.txt')
for line in commands:
    output = net_connect.send_command(line, strip_command=False)
    print(output) 
    print("*"*64) 
    print(" ")
commands.close()

print("\n"*3)
print("#"*42)
print("###!ThIS IS THE END OF DATA COLLECTION!###")
print("#"*42)

