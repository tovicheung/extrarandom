import random as _random
import string as _string

class ExtraRandom(_random.Random):
    def randbool(self):
        """Returns a random boolean"""
        return bool(self.randint(0, 1))
    
    def randbools(self, n=1):
        """Returns a list of random booleans"""
        return [self.randbool() for _ in range(n)]
    
    def randletter(self):
        """Returns a random letter (uppercase and lowercase)"""
        return self.choice(_string.ascii_letters)
    
    def randuppercase(self):
        """Returns a random uppercase letter"""
        return self.choice(_string.ascii_uppercase)
    
    def randlowercase(self):
        """Returns a random lowercase letter"""
        return self.choice(_string.ascii_letters)
    
    def randhex(self, a, b):
        """Return random hex in range [a, b], including both end points.
        
        a and b should be a hex number too (str actually)"""
        try:
            a = int(a, 16)
            b = int(b, 16)
        except ValueError:
            raise ValueError("randhex() only accepts hex numbers in the form of a string") from None
        return hex(self.randint(a, b))
    
    def strinsert(self, string: str, substring: str):
        """Inserts substring into string at a random position
        
        Substring could be inserted at the start and end of string
        Use strinsertin() to prevent this
        """
        pos = self.randint(0, len(string))
        return string[:pos] + substring + string[pos:]
    
    def strinsertin(self, string: str, substring: str):
        """Inserts substring into string at a random position inside the string
        ie not at the start/end"""
        pos = self.randrange(1, len(string))
        return string[:pos] + substring + string[pos:]
    
    def listinsert(self, x: list, element): # todo: add optional argument n for inserting multiple times
        """Randomly inserts element into list x in place, and return None
        
        Element could be inserted to the start/end of list
        Use listinsertin() to prevent this"""
        index = self.randint(0, len(x))
        x.insert(index, element)
    
    def listinsertin(self, x: list, element):
        """Randomly inserts element into list x in place, and return None
        
        Element will not be inserted to the start/end of list"""
        index = self.randint(0, len(x))
        x.insert(index, element)

    def randattr(self, x):
        return self.choice(dir(x))
    
    def getrandattr(self, x):
        return getattr(x, self.randattr(x))
    
    def setrandattr(self, x, value):
        """Not very useful tho"""
        setattr(x, self.randattr(x), value)
    
    def delrandattr(self, x):
        delattr(x, self.randattr(x))

    def permutation(self, iterable, r=None):
        pool = tuple(iterable)
        r = len(pool) if r is None else r
        return tuple(self.sample(pool, r))
    
    def combination(self, iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        indices = sorted(self.sample(range(n), r))
        return tuple(pool[i] for i in indices)
    
_inst = ExtraRandom()
randbool = _inst.randbool
randbools = _inst.randbools
randletter = _inst.randletter
randhex = _inst.randhex
randuppercase = _inst.randuppercase
randlowercase = _inst.randlowercase
strinsert = _inst.strinsert
strinsertin = _inst.strinsertin
listinsert = _inst.listinsert
listinsertin = _inst.listinsertin
randattr = _inst.randattr
getrandattr = _inst.getrandattr
setrandattr = _inst.setrandattr
delrandattr = _inst.delrandattr
permutation = _inst.permutation
combination = _inst.combination

__all__ = []
for _name in globals().keys():
    if not _name.startswith("_"):
        __all__.append(_name)
