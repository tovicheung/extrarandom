"""extrarandom: more utilities for random
This module is built on top of the builtin random module
"""

import random
import string

class ExtraRandom(random.Random):
    def randbool(self):
        """Returns a random boolean"""
        return bool(self.randint(0, 1))
    
    def randbools(self, n=1):
        """Returns a list of random booleans"""
        return [self.randbool() for _ in range(n)]
    
    def randletter(self):
        """Returns a random letter (uppercase and lowercase)"""
        return self.choice(string.ascii_letters)
    
    def randuppercase(self):
        """Returns a random uppercase letter"""
        return self.choice(string.ascii_uppercase)
    
    def randlowercase(self):
        """Returns a random lowercase letter"""
        return self.choice(string.ascii_letters)
    
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
