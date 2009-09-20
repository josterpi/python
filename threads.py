
from threading import Thread
from time import sleep
import random

def do_stuff(name):
    for i in range(5):
        print name, i
        sleep(0.1 * random.randint(1,10))

a = Thread(target=do_stuff, args=('a',))   
b = Thread(target=do_stuff, args=('b',))   
c = Thread(target=do_stuff, args=('c',))   

a.start()
b.start()
c.start()
