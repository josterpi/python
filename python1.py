#!/usr/bin/env python

# initialized at 1, I have two actions I can do on the number
# line. I can jump forward and jump backwards.
# The jump forward is 2*current position + 1
# The jump back is the current position - 3
# Can you hit all of the integers?
# If not, what can't you hit? What can you? Any patterns?
# When you're jumping back, what's the last positive integer you can hit?
# 
# As you jump back from a position, eventuallly you'll hit a number you've
# hit before. From then on, you won't get any new numbers.
# Given a number, where will you hit an already hit number?
#
# Going back from a number, what is the ratio of hits to misses?
#
# If you want to hit every number you can up to n, how far forward of n
# do you have to go?
# Something like:
# [(2,4),(3,9),(4,16),(5,33),(6,64),(7,129),(8,256),(9,513),(10, 1024)]


import sys

class Jumper:
    def __init__(self):
        self.current = 1
        self.print_me = False
        self.hit = [1]
    def forward(self):
        self.current = 2*self.current+1
        if self.current not in self.hit:
            self.hit.append(self.current)
            self.hit.sort()
        if self.print_me:
            print self.current
    def back(self):
        self.current = self.current - 3
        if self.current not in self.hit:
            self.hit.append(self.current)
            self.hit.sort()
        if self.print_me:
            print self.current
    def printing(self):
        self.print_me = True
    def noprinting(self):
        self.print_me = False
    def reset(self,n = 1):
        self.current = n
    def __repr__(self):
        return str(self.current) + "\n" + str(self.hit)
    
def forward(n):
    return 2*n+1

def back(n):
    return n-3

def forward_range(n):
    current = 1
    fseq = [1]
    for i in range(n):
        current = forward(current)
        fseq.append(current)
    return fseq

def add_forward(seq, n):
    current = seq[-1]
    for i in range(n):
        current = forward(current)
        seq.append(current)
    return seq

def main():
	seq = forward_range(int(sys.argv[1]))
	print seq
	nline = forward_range(int(sys.argv[1]))
	for i in seq:
		hit = miss = first_miss = last_miss = 0
		h_m = -1
		j = back(i)
		print "----------------------------------"
		print j
		while j>1:
			if nline.count(j)==0:
				nline.append(j)
				hit = hit + 1
			else:
				if (miss == 0):
					first_miss = j
				if j==3 or j==4:
					last_miss = j
				miss = miss + 1
			j = back(j)
		if miss != 0:
			h_m = float(hit)/miss
		print "hits:       ",hit
		print "misses:     ",miss
		print "h/m:        ",h_m
		print "first miss: ",first_miss
		print "last miss:  ",last_miss
	nline.sort()
	print nline

if __name__ == '__main__':
	main()
