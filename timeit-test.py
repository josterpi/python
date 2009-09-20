
import random

def subtract(s1, s2):
    result = list(s1)
    for i, element in enumerate(s2):
        if element in result:
            del result[i]
    return result

a = []
for i in range(20):
    a.append(object())

b = []
for i in range(5):
    b.append(random.choice(a))

def test():
    subtract1(a,b)

if __name__=='__main__':
    from timeit import Timer
    t = Timer("test()", "from __main__ import test")
    print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000)
