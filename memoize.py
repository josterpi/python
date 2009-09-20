
class memoize(object):
    """
    Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned,
    and not re-evaluated
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
                self.cache[args] = value = self.func(*args)
                return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument
            return self.func(*args)
     def __repr__(self):
         "Return the function's docstring."
         return self.func.__doc__

def fibonacci(n):
    "Return the nth fibonacci number"
    if n in (0,1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)
