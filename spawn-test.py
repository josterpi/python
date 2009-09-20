#!/usr/bin/env python24

import os

print "about to spawn..."
os.spawnl(os.P_NOWAIT, '/home/josterpi/docs/csci/python/child-of-spawn.py')
print "done..."
