#!/usr/bin/python3

# USE AT YOUR OWN RISK. BACKUP YOUR DATABASE BEFORE USING THIS PROGRAM.

# see readme.md for instructions on how to use this program

from time import sleep
from re import search, sub
from datetime import datetime

infile='infile.json'
outfile='outfile.json'

# def printf(*s):
    # print(s,end='')

with open(outfile, 'w') as o:
    o.writelines('')

with open(infile, 'r') as f:
    f.readline()
    line = f.readline()
    if search(r"\"system_config\"", line):
        with open(outfile, 'a') as o:
            o.writelines('{' + '\n')
            o.writelines('\t"systemConfig":' + '\n')
            o.writelines('\t{' + '\n')

            f.readline()
            f.readline()

            line = f.readline()
            s = search(r"(?P<ee>\".*\"): ?(?P<value>\".*\")", line).groupdict()
            o.writelines('\t\t"motd": {}'.format(s['value']) + ',\n')
            o.writelines('\t\t"tags": []\n')
            o.writelines(f.readline()[:-1] + ',\n')
            f.readline()
    while(1):
        line = f.readline()
        if not search(r"\"joined\"|\"left\"|lastActive|cooldownUntil|warnExpiry", line):
            with open(outfile, 'a') as o:
                o.writelines(line)
            continue
        if line.split(':', 1)[1].find('null') != -1:
            with open(outfile, 'a') as o:
                o.writelines(line)
            continue
        s = search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\s+" + 
                   "(?P<hour>\d{2}):(?P<min>\d{2}):(?P<sec>\d{2})", line).groupdict()
        #datetime()
        print(line)
        stamp = str(int(datetime(int(s['year']),
                             int(s['month']),
                             int(s['day']),
                             int(s['hour']),
                             int(s['min']),
                             int(s['sec'])).timestamp()))
        with open(outfile, 'a') as o:
            o.writelines(sub(r"(?<=: )\".*\"", stamp, line))
