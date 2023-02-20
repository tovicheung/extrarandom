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