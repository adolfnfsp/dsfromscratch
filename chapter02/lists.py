# ordered collection
interger_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [interger_list, heterogeneous_list, []]

list_length = len(interger_list)    # equals 3
list_sum = sum(interger_list)       # equals 6

# get or set nth element
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]     # equals 0, ists are 0-indexed
one = x[1]      # equals 1
nine = x[-1]    # equals 9, 'Pythonic' for last element
eight = x[-2]   # equals 8, 'Pythonic' for next-to-last element
x[0] = -1       # now x is [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slice lists with slice i:j (elements from i-inclusive to j-not inclusive)
first_three = x[:3]             # [-1, 1, 2]
three_to_end = x[3:]            # [3, 4, 5, 6, 7, 8, 9]
one_to_four = x[1:5]            # [1, 2, 3, 4]
last_three = x[-3:]             # [7, 8, 9]
without_first_and_last = x[1:-1]# [1, 2, 3, 4, 5, 6, 7, 8]
copy_of_x = x[:]                # [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slice can take a third argument indicating stride
every_third = x[::3]            # [-1, 3, 6, 9]
five_to_three = x[5:2:-1]       # [5, 4, 3]

# checking membership with in, output is boolean
print(1 in [1, 2, 3])   # True
print(0 in [1, 2, 3])   # False

# concatenating lists
x = [1, 2, 3]
x.extend([4, 5, 6]) # x is now [1, 2, 3, 4, 5, 6]

x = [1, 2, 3]
y = x + [4, 5, 6]   # x is unchanged

x = [1, 2, 3]
x.append(0)     # appending one item at a time, x is now [1, 2, 3, 0]
y = x[-1]       # y equals 0
z = len(x)      # equals 4

x , y = [1, 2]  # unpack lists, now x is 1, y is 2
# must have same numbe of elements on both sides otherwise ValueError
_, y = [1, 2]   # underscore for value you will throw away, now y is 2



