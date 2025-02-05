"""
Iterables and Generators
"""

class IterGens:
    """some docstring"""
    # contructor
    def __init__(self):
        """initializing the class"""
        pass

    # representational string method
    def __repr__(self):
        """string representation of a class instance"""
        pass

    def generate_range(n):
        pass
# skip the above class definition

# more optimized way of generating part of lists on demand
def generate_range(n):
    i = 0
    while i < n:
        yield i     # every call to yield produces a value of the generator lazily
        i += 1

# consuming yielded values one at a time until none are left:
for i in generate_range(10):
    print(f"i: {i}")

# can even optimally generate an infinite sequence
def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1
        if n > 100: # rudimentary termination fo infinite loop
            break

# second way to create generators using for comprehensions
evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

# None of these computations *does* anything until we iterate
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# and so on

# iterate while getting values and indices using enumerate function
names = ["Alice", "Bob", "Charlie", "Debbie"]

# not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {name[i]}")
    i += 1

# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")


