"""
Randomness
"""

# generating random numbers
import random
random.seed(10)     # this ensures we get the same reuslts every time (pseudorandom)

four_uniform_randoms = [random.random() for _ in range(4)]

# [0.5714025946899135,  # random.random() produces numbers
# 0.4288890546751146,   # uniformly between 0 and 1.
# 0.5780913011344704,   # It's the random function we'll use
# 0.20609823213950174]  # most often.

# to get pseudorandom numbers, reproducing the random numbers
random.seed(10)         # set the seed to 10
print(random.random())  # 0.5714025946899135
random.seed(10)         # reset the seed to 10
print(random.random())  # 0.5714025946899135 again

print(random.randrange(10))    # choose randomly from range(10) = [0 ,1 , ..., 9]
random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)   # randomly reorders elements in a list
print(up_to_ten)

my_best_friend = random.choice(["Alice", "Bob", "Charlie"]) # randomly picks an element
print(my_best_friend)

# randomly choose a sample of elements without replacement (i.e., with no duplicates)
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [random sample without replacement]
print(winning_numbers)

# random sample with replacement
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)    # 
