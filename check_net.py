#!/usr/bin/env python

import os
import commands
import time
import re

def ping_google():
        ping = commands.getoutput('ping google.com -c5 -q')
        if (re.search("[1-5] received",ping)):
                print "Ping google succeeded"
                return True
        return False

def inet_restart():
        print "Restarting internet"
        os.system('/etc/rc.d/rc.inet1 stop')
        time.sleep(10)
        os.system('/etc/rc.d/rc.inet1 start')

count = 5
# ping google
# if there's a reply, end
# if not, wait 1 minute and try again
# after five tries, restart internet. sleep for 2 minutes
# if we've restarted the internet, repeat
while count == 5:
        count = 0
        # check for pong from google. check 5 times, or first response
        while (not ping_google() and count < 5):
                time.sleep(60)
                count += 1
        if count == 5: #can't get a hold of google within five minutes
                inet_restart()
                time.sleep(120)

