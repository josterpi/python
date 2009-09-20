
def add(a, b):
    """
    >>> add(1,2)
    3
    >>> add(1,1)
    2
    """
    return a + b

def divide(a, b):
    """
    >>> divide(4,2)
    2
    >>> divide(4,0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
        File "testdoctest.py", line 12, in divide
            return a / b
    ZeroDivisionError: integer division or modulo by zero
    """
    return a / b
__test__ = {
    'compose add(divide())': 
        """
        >>> divide(add(2,2),2)
        2
        """,
    'compose add(divide()) (built to fail)': 
        """
        >>> divide(add(2,2),2)
        22
        """,
}
        

def _hidden():
    """
    >>> _hidden()
    "You can't see me, doctest!"
    """
    return "You can't see me, doctest!"

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    _test()
