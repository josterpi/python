
def gcd(a, b):
    """
    Returns the greatest commond divisor of a and b.
    Input:
        a -- an integer
        b -- an integer
    Output:
        an integer, the gcd of a and b
    Examples:
    >>> gcd(97,100)
    1
    >>> gcd(97 * 10**15, 19**20 * 97**2)
    97L
    """
    if a < 0:  
        a = -a
    if b < 0:  
        b = -b
    if a == 0: 
        return b
    if b == 0: 
        return a
    while b != 0: 
        a = b
        b = a % b
    return a

def xgcd(a, b):
    """
    Returns g, x, y such that g = x*a + y*b = gcd(a,b).
    Input:
        a -- an integer
        b -- an integer
    Output:
        g -- an integer, the gcd of a and b
        x -- an integer
        y -- an integer
    Examples:
    >>> xgcd(2,3)
    (1, -1, 1)
    >>> xgcd(10, 12)
    (2, -1, 1)
    >>> g, x, y = xgcd(100, 2004)
    >>> print g, x, y
    4 -20 1
    >>> print x*100 + y*2004
    4
    """
    if a == 0 and b == 0: return (0, 0, 1)
    if a == 0: return (abs(b), 0, b/abs(b))
    if b == 0: return (abs(a), a/abs(a), 0)
    x_sign = 1; y_sign = 1
    if a < 0: a = -a; x_sign = -1
    if b < 0: b = -b; y_sign = -1
    x = 1; y = 0; r = 0; s = 1
    while b != 0:
        (c, q) = (a%b, a/b)
        (a, b, r, s, x, y) = (b, c, x-q*r, y-q*s, r, s)
    return (a, x*x_sign, y*y_sign)

def inversemod(a, n):
    """
    Returns the inverse of a modulo n, normalized to
    lie between 0 and n-1.  If a is not coprime to n,
    raise an exception (this will be useful later for 
    the elliptic curve factorization method).
    Input:
        a -- an integer coprime to n
        n -- a positive integer
    Output:
        an integer between 0 and n-1.
    Examples:
    >>> inversemod(1,1)
    0
    >>> inversemod(2,5)
    3
    >>> inversemod(5,8)
    5
    >>> inversemod(37,100)
    73
    """
    g, x, y = xgcd(a, n)
    if g != 1:
        raise ZeroDivisionError, (a,n)
    assert g == 1, "a must be coprime to n."
    return x%n

def lcm(a, b):
    return (a * b) / gcd(a, b)

class EuclidLine(object):
    def __init__(self, a, b):
        self.dividend = a
        self.divisor = b
        self.remainder = a % b
        self.quotient = a / b
    def __repr__(self):
        return "<EuclidLine: %i = %i - %i x %i>" % (self.remainder, self.dividend, self.quotient, self.divisor)

# elist.append(EuclidLine(120, 23))
# elist.append(EuclidLine(elist[-1].divisor, elist[-1].remainder))

def rsa_setup(p, q):
    # n is the modulus
    n = p * q
    phi = (p-1) * (q-1)
    # Public is an integer e such that 1 < e < phi and gcd(e, phi) = 1
    # For now, we can just pick one
    public = 23
    private = inversemod(public, phi)

    return {'public': public, 'private': private, 'modulo': n}

def rsa_encrypt(message, public, modulo):
    return message ** public % modulo

def rsa_decrypt(message, private, modulo):
    return message ** private % modulo
