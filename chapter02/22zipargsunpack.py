"""
zip and Argument Unpacking
"""
# zip two or more iterables together
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy, so you have to do something like the following
[pair for pair in zip(list1, list2)]    # is [('a', 1), ('b', 2), ('c', 3)]
# preferable to have lists of the same length

# can also unzip
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
# similar to if you called
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

# can use argument unpacking with any function
def add(a, b): return a + b

print(add(1, 2))       # returns 3
try:
    print(add([1, 2]))
except TypeError:
    print("add expects two inputs")
print(add(*[1, 2]))            # returns 3
# will rarely use this, however neat trick
