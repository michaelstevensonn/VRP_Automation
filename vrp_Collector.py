#!/usr/bin/env python
import netmiko
import json
import os
import sys
import time



timestr = time.strftime("%Y%m%d_%H%M%S")
outputfile = timestr + '-output.log'
connection = netmiko.ConnectHandler(ip='192.168.99.77', device_type='linux', 
                                username='Michael', password='65831120341Myt')

output=open(outputfile,'a')

print(connection.send_command('cat /etc/os-release'),file=output)
print(" ",file=output)
print("="*64,file=output)
print(" ",file=output)
print(connection.send_command('uname -a'),file=output)
print(" ",file=output)
print("="*64,file=output)
print(" ",file=output)
print(connection.send_command('ls -al'),file=output)
print(" ",file=output)
print("="*64,file=output)
print(" ",file=output)
print(connection.send_command('ls -R /usr '), file=output)
print(" ",file=output)
print("="*64,file=output)
print(" ",file=output)
print(connection.send_command('ls -R /etc '), file=output)
print("\n"*3,file=output)
print("#"*42,file=output)
print("###!ThIS IS THE END OF DATA COLLECTION!###",file=output)
print("#"*42,file=output)
output.close()

connection.disconnect()

