'''
Some boolean ideas
'''

one_is_less_than_two = 1 < 2        # equals True
print(one_is_less_than_two)
true_equals_fales = True == False   # equals False
print(true_equals_fales)

# None indicates nonexistent value
x = None
assert x == None, "this is not the Pythonic was to check for None"
assert x is None, "this is the Pythonic way to check for None"

# empties and zeroes are treated as False, otherwise are True
def some_function_that_returns_a_string():
    return "Adolf"

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
    print(first_char)
else:
    first_char = ""
    print(first_char)

# confusing equivallent of doing the above
first_char = s and s[0]
print(first_char)

safe_x = x or 0
print(safe_x)

safe_x = x if x is not None else 0 # more readable version of statement 31
print(safe_x)

# the all() and any() functions
print(all([True, 1, {3}])) # True, all are truthy
print(all([True, 1, {}]))  # False, {} is falsy
print(any([True, 1, {}]))  # True, True is truthy
print(all([]))             # True, no falsy elements in the list
print(any([]))             # False, no truthy elements in the list