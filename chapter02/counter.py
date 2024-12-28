# Counters
# defaultdict(int)-like object mapping keys to counts:
from collections import Counter
c = Counter([0, 1, 2, 0])           # c is (basically) {0: 2, 1: 1, 2: 1} simple
                                    # way to solve our word_counts problem
# # recall, document is a list of words
# word_counts = Counter(document)

# most common useful method in Counter
# # print the 10 most common words and their counts
# for word, count in word_counts.most_common(10):
#     print(word, count)