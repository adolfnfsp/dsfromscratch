"""
Type Annotations
"""

# Python doesn't care about the types of objects
# as long as we use them in valid ways

def add(a, b):
    return a + b

assert add(10, 5) == 15,                        "+ is valid for numbers"
assert add([1, 2], [3]) == [1, 2, 3],           "+ is valid for lists"
assert add("hi ", "there"),                     "+ is valid for strings"

try:
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")

# statically typed languages, functions and objects would have specific types:
def add1(a: int, b: int) -> int:
    return a + b

print(add1(10, 5))             # you'd like this to be OK
print(add1("hi ", "there"))    # you'd like this to be not OK

"""
There are good reasons to use type annotations in code:
1. makes code informative
2. forces to design cleaner functions and interfaces
3. allows the editor to help with things like autocomplete
   and to get angry at type errors
4. Though 'type hints' preferred on large projects, recommended even for
   small projects, with the help of a good editor app
"""

"""How to Write Type Annotations"""

# using the typing module
from typing import List # not capital L

def total(xs: List[float]) -> float:
    return sum(total)
# type annotation for fuction parameters and return types

# This is how to type-annotate variable when you define them.
# But this is unnecessary; it's "obvious" x is an int.
x: int = 5

# Situations where it is not obvious
values = []         # what's my type?
best_so_far = None  # what's my type?

# we supply inline type hints:
from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None # allowed to be either a float or None

# other examples
from typing import Dict, Iterable, Tuple

# keys are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

# lists and generators are both iterable
lazy: bool = False
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 ==0)
else:
    evens = [0, 2, 4, 6, 8]

# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)

# Since Python has first class functions:
from typing import Callable

# The type hint says that repeater is a function that takes
# two arguments, a string and an int, and returns a string.
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"

# type annotations can be assigned to variables, making them
# easier to refer to:

Number = int
Numbers = List[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)

# I hope I will get used to these type annotations.
