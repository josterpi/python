
import timeit

class Foo(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4

class Wrapper(object):
    def __init__(self, object, new_attrs):
        self.object = object
        self.new_attrs = list(new_attrs) + ['object']
    def __getattribute__(self, attr):
        if attr in object.__getattribute__(self, 'new_attrs'):
            return object.__getattribute__(self, attr)
        else:
            return object.__getattribute__(object.__getattribute__(self,'object'), attr)
    # Overriding __setattr__ is very expensive
    #def __setattr__(self, attr, value):

f = Foo()
b = Wrapper(f,('foo','bar'))
def t1():
    f.a
    f.b
    f.c
    f.d

def t2():
    b.a
    b.b
    b.c
    b.d

def main():
    f = Foo()
    b = Wrapper(f,('foo','bar'))
    b.foo = "foo"
    T = timeit.Timer("t1()", "from __main__ import t1")
    print T.repeat(5, 1)

if __name__ == '__main__':
    main()
