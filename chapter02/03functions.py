# def double(x):
#     """
#     This is where you put an optional docstring that explains what the
#     function does. For example, this function multiplies its input by 2.
#     """
#     return x * 2

# # need to understand from here more, function being first class?
# def apply_to_one(f):
#     """Calls the function f with 1 as its argument"""
#     return f(1)

# my_double = double          # refers to the previously defined function
# x = apply_to_one(my_double) # equals 2
# print(my_double, ",", x)

# # short anonymous functions or lambdas
# y = apply_to_one(lambda x: x + 4) # equals 5
# print(y)

# # can assign lambdas to variables, but not good practice
# another_double = lambda x: 2 * x    # don't do this
# print(another_double)

# def another_double(x):
#     """Do this instead"""
#     return 2 * x

# print(another_double)
# # need to understand above, function being first class, lambda functions?

# # function with given default arguments
# def my_print(message = "my default message"):
#     print(message)

# my_print("hello")   # prints 'hello'
# my_print()          # prints 'my default message'

# # useful sometimes to specify arguments by name
# def full_name(first = "What's-his-name", last = "Something"):
#     return first + " " + last

# print(full_name("Adolf", "Rutebeka"))  # "Adolf Rutebeka"
# print(full_name("Adolf"))              # "Adolf Something"
# print(full_name(last="Rutebeka"))      # "What's-his-name Rutebeka"

# version 2: Functions
def double(x):
    """
    This is where you put an optional socstring that explains what the
    function does. For example, this function multiplies its input by 2.
    """
    return x * 2

# python functions are first-class, need to understand this more
def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return f(1)

my_double = double                  # refers to the previously defined function
x = apply_to_one(my_double)         # equals 2

# short anonymous functions, lambdas
y = apply_to_one(lambda x: x + 4)   # equals 5

another_double = lambda x: 2 * x    # don't do this

def another_double(x):
    """Do this instead"""
    return 2 * x

def my_print(message = "my default message"):
    print(message)

my_print("hello")      # prints 'hello'
my_print()             # prints 'my default message'

def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

full_name("Joel", "Grus")       # "Joel Grus"
full_name("Joel")               # "Joel Something"
full_name(last="Grus")          # "What's-his-name Grus"