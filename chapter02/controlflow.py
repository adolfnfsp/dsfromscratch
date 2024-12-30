'''
performing action conditionally
'''
if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

# a ternary if
x = 0
parity = "even" if x % 2 == 0 else "odd"

# while loop
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1

# often we use for and in
# range (10) is the number 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10")

# complex logic with continue and break
for x in range(10):
    if x == 3:
        continue    # go immediately to the next iteration
    if x == 5:
        break       # quit the loop entirely
    print(x)        # will print 0, 1, 2, and 4
