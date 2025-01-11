'''
Lesson in sorting
'''
# Python list has a sort method
x = [4, 1, 2, 3]
y = sorted(x)       # y is [1, 2, 3, 4], x is unchanged
x.sort()            # now x is [1, 2, 3, 4]

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]

# sort the words and counts from highest count to lowest
from collections import Counter
words = '''
this is not a very good example to begin counting words in this example,
I guess we shall see how it works.
'''
word_counts = Counter(words)
wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)
print(wc)