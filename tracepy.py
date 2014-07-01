#!/bin/bash
import os

for i in range(255): # Enter range here
    ip = "192.168.1.%d" % (i) # Enter range here
    response = os.system("traceroute -z 10 " + ip) # traceroute with a 10 sec delay

    print ip



