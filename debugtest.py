
import inspect


class Test(object):
    pass

def test():
    a = Test()
    b = inspect.currentframe()
    print b.f_code.co_filename
    print b.f_code.co_name


test()
