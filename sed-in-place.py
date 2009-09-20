#!/usr/bin/python -O

import sys
import re

f = file('test.txt','rw+')

f.write('11111blablabala\n')
for line in f:
    f.write('blablabala\n')
    #if re.match('replace\n',line):
f.write('2222222222222\n')

f.close()
