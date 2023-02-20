from extrarandom import randbool, randhex

assert isinstance(randbool(), bool)

try:
    randhex("p", 8)
except ValueError as e:
    ...
except:
    assert False
else:
    assert False

assert randhex(hex(9), hex(9)) == hex(9)
