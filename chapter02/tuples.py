# list immutable cousins
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3      # now my_list = [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

# tuples convenient to return multiple values
def sum_and_product(x, y):
    return (x + y), (x * y)
sp = sum_and_product(2, 3)      # sp is (5, 6)
s, p = sum_and_product(5, 10)    # s is 15, p is 50

# can be used for multiple assignment
x, y = 1, 2     # x is 1, y is 2
x, y = y, x     # Pythonic way to swap variables: x is 2, y is 1
