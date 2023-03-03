from random import choice
from .extrarandom import randbool

class randiter:
    """Iterator that returns random elements from iterable"""
    def __init__(self, iterable, total=-1):
        self.__iterable = iterable
        self.__total = total

    def __iter__(self):
        self.__n = 0
        return self
    
    def __next__(self):
        self.__n += 1
        if self.__n > self.__total and self.__total != -1:
            raise StopIteration
        return choice(self.__iterable)
    
class randboolstream:
    def __iter__(self):
        return self
    
    def __next__(self):
        return randbool()

# _exclude = ["choice"]
# __all__ = list(globals().keys())
# for name in _exclude:
#     __all__.remove(name)
# del name
