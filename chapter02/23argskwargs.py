"""
args and kwargs
"""

# Let us look at some examples of function arguments and keyword arguments
def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)
    
    # And return that new function
    return g

# This works in some cases:
def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8, "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

# However, it does not work with functions taking more than a single argument:
def f2(x, y):
    return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")

# we need to define function that takes arbitrary arguments
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")

# prints
# unnamed args: (1, 2)
# keyword args: {'key': 'word', 'key2': 'word2'}

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1, 2, 3 should be 6"

# we will use this to produce higher order functions whose inputs
# can be arbitrary arguments

def doubler_correct(f):     # improvement to the previous doubler.
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"

# we use args and kwargs only when we have no other option.
