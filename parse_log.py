#!/usr/bin/python -O

LOG_ENTRY='156.34.26.230 - - [09/Feb/2006:18:23:47 +0000] "GET /Top10Bookmarked?agent=ext HTTP/1.1" 200 107'

import re
import datetime
import sys

MONTHS = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

class LogEntry:
	def __init__(self, ip, day, month, year, hour, minute, second, request, status, size):
		self.ip = ip
		#self.day = int(day)
		#self.month = month
		#self.year = int(year)
		#self.hour = int(hour)
		#self.minute = int(minute)
		#self.second = int(second)
		self.request = request
		self.status = int(status)
		self.size = int(size)
		self.tstamp = datetime.datetime(int(year), MONTHS[month], int(day), int(hour), int(minute), int(second))

	def __repr__(self):
		return "%s - - [%s +0000] \"%s\" %d %d" % (self.ip, self.tstamp.strftime('%d/%b/%Y:%H:%M:%S'), self.request, self.status, self.size)

class LogFile:
    def __init__(self, logfile):
        infile = file(logfile,"r")
        log_splitter = re.compile('([\d.]*) \- \- \[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) \+0000\] "([\w/?=.+%& ]*)" (\d*) (\d*)')
        self.entries = []
        for line in infile:
            log_match = log_splitter.match(line)
            self.entries.append(LogEntry(log_match.group(1), log_match.group(2), log_match.group(3), log_match.group(4), log_match.group(5), log_match.group(6), log_match.group(7), log_match.group(8), log_match.group(9), log_match.group(10)))
        infile.close()

def main():
    pass

if __name__ == '__main__':
	main()
