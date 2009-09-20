#!/usr/bin/env python

import time
import signal

def nohup(signum, frame):
    return

signal.signal(signal.SIGHUP, nohup)

print "going to sleep..."
time.sleep(10)
print "done..."
