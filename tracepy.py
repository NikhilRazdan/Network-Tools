#!/bin/bash
import os

for i in range(160):
    ip = "5.199.175.%d" % (i)
    response = os.system("traceroute -z 10 " + ip)
    print ip



