# # associate values with keys and quickly retrieve the value corresponding to a given key

# empty_dict = {}                     # Pythonic
# empty_dict2 = dict()                # less Pythonic
# grades = {"Adolf": 80, "Joel": 95}  # dictionary literal

# joels_grade = grades["Joel"]        # equals 95

# # gets KeyError if ask for key not in the dictionary
# try:
#     kates_grade = grades["Kate"]
# except KeyError:
#     print("no grade for Kate!")

# # can check for existence of key, fast even for large dictionaries
# joel_has_grade = "Joel" in grades   # True
# kate_has_grade = "Kate" in grades   # False
# print("{1}, {0}".format(joel_has_grade, kate_has_grade))

# # recommended to use get method, as handles better keys not present
# joels_grade = grades.get("Joel", 0)     # equals 80
# kates_grade = grades.get("Kate", 0)     # equals 0
# no_ones_grade = grades.get("No One")    # default is None
# print(f"{joels_grade}, {kates_grade}, {no_ones_grade}")

# # assing key/value pairs
# grades["Kate"] = 100        # adds a third entry
# grades["Adolf"] = 97        # replaces/modifies the old value
# num_students = len(grades)  # equals 3
# print(f"{num_students}, {grades['Adolf']}, {grades['Kate']}")

# # dictionaries to represent structured data
# tweet = {
#     "user" : "joelgrus",
#     "text" : "Data Science is Awesome",
#     "retweet_count" : 100,
#     "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
# }
# print(tweet)
# # can look at all the keys
# tweet_keys = tweet.keys()       # iterable for the keys
# tweet_values = tweet.values()   # iterable for the values
# tweet_items = tweet.items()     # iterable for the (key, value) tuples

# print("user" in tweet_keys)            # True, but not Pythonic
# print("user" in tweet)                 # Pythonic way of checking for keys
# print("joelgrus" in tweet_values)      # True (slow but the only way to check)

# # defaultdict

# version 2: Dictionaries
# associate values with keys, quickly retrieve value corresponding to a key
empty_dict = {}                         # Pythonic
empty_dict2 = dict()                    # less Pythonic
grades = {"Joel": 80, "Tim": 95}        # dictionary literal

# look up value of a key with square brackets: get KeyError if key not in
joels_grade = grades["Joel"]            # equalsd 80

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# check existence of key: fast even for large dict
joel_has_grade = "Joel" in grades       # True
kate_has_grade = "Kate" in grades       # False

# using get method, robust to exceptions
joels_grade = grades.get("Joel", 0)     # equals 80
kates_grade = grades.get("Kate", 0)     # equals 0
no_ones_grade = grades.get("No one")    # default is None

# assign key/value pairs
grades["Tim"] = 99                      # replaces the old value
grades["Kate"] = 100                    # adds a third entry
num_students = len(grades)              # equals 3

# dicts to respresent structured data
tweet = {
    "user": "joelgrus",
    "test": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"] 
}

# look at all of the keys
tweet_keys = tweet.keys()       # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items = tweet.items()     # iterable for the (key, value) tuples

"user" in tweet_keys            # True, but not Pythonic
"user" in tweet                 # Pythonic way of checking for keys
"joelgrus" in tweet_values      # True (slow bu the only way to check)

# defaultdict
from collections import defaultdict

# word_counts = defaultdict(int)          # int() produces 0
# for word in document:
#     word_counts[word] += 1
# # similar to
# word_counts = {}
# for word in document:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
# # similar to "forgiveness is better than permission"
# word_counts = {}
# for word in document:
#     try:
#         word_counts[word] += 1
#     except KeyError:
#         word_counts[word] = 1
# # similar to "graceful with missing keys"
# word_counts = {}
# for word in document:
#     previous_count = word_counts.get(word, 0)
#     word_counts[word] = previous_count + 1

# defaultdict can be useful with list or dict, or even your own functions:
dd_list = defaultdict(list)                 # list() produces an empty list
dd_list[2].append(1)                        # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)                 # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"         # {"Joel": {"City": "Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                           # now dd_pair contains {2: [0, 1]}
