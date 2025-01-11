'''
Automated testing and assert
'''
assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"

# assert funchions do what is expected, highly encouraged to use this way
def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1

def smallest_item2(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)

print(smallest_item2([2, 3, 4, 5]))
print(smallest_item2([]))
