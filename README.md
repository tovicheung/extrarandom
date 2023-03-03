# extrarandom
A library that provides extra utilities builtin on the builtin library `random`.

## Installation
`pip install extrarandom`

## Methods
Random booleans
```py
some_bool = randbool()
three_bools = randbools(3)
```

Random characters
```py
letter = randletter()
uppercase = randuppercase()
lowercase = randlowercase()
```

Random hex
```py
nine = hex(9)
twenty = hex(20)
sth_between_9_and_20 = randhex(nine, twenty) # returns a string just like hex()
```

Random string manipulation
```py
mystring = "abcdef"
modified_string = strinsert(mystring, "HELLO")
# some possible outcomes:
# "abHELLOcdef", "HELLOabcdef", "abcdefHELLO", etc

# if you don't want the substring to be inserted at the start/end:
modified_string2 = strinsertin(mystring, "HELLO")
# impossible outcomes:
# "HELLOabcdef", "abcdefHELLO"
```

Random list manipulation
```py
mylist = [1, 2, 3, 4]
listinsert(mylist, -999)
# some possible outcomes:
# [-999, 1, 2, 3, 4] [1, 2, -999, 3, 4] [1, 2, 3, 4, -999]

# listinsertin is similar to strinsertin
```

Random permutation/combination
```py
perm = permutation(iterable)
comb = permutation(iterable)
```

Range objects
```py
some_range_between_6_and_9 = subrange(range(6, 9))
# possible values:
# range(6, 7), range(6, 9), range(8, 9) etc.
# start will not be equal to stop
```

Random iteration
```py
mylist = [1, 2, 3, 4, 5]
for i in randiter(mylist, total=8):
    print(i)
# print 8 random elements from mylist
```

## Not so useful stuff (yet)

Infinite iterators
```py
for b in randboolstream():
    print(b)
# infinite random boolean stream lol
```

Random attribute manipulation (not too useful tho)
```py
getrandattr(obj)
setrandattr(obj, value)
delrandattr(obj)
```