#!/usr/bin/env python

import os

output = os.popen("xsetwacom  --list devices 2>/dev/null").read().replace('\t',' ').split("\n") 
for line in output:
    if len(line)>20:
        pp = [t for t in line.split(" ") if len(t)>0]
        num = pp[7]
        cmd = f"xsetwacom --set {num} Area 0 0 89600 29600"
        print(cmd)
        os.popen(cmd)



