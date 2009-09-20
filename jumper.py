def forward(n):
	return n*2 + 1

def back(n):
	return n-3
print back(forward(1))

current = 1  
for i range(10):
	current = back(forward(current))
	print current

current = 1 
for i in range(5):
	current = forward(current)
	print current

def forward_times(n):
	c = 1
	for i in range(n):
		c = forward(c)
		print c
	return c

def back_to_zero(n):
	while n>0:
		n = back(n)
		print n

# 0,1,3,4,6,7,9,10
