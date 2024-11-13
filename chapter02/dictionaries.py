# associate values with keys and quickly retrieve the value corresponding to a given key

empty_dict = {}                     # Pythonic
empty_dict2 = dict()                # less Pythonic
grades = {"Adolf": 80, "Joel": 95}  # dictionary literal

joels_grade = grades["Joel"]        # equals 95

# gets KeyError if ask for key not in the dictionary
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# can check for existence of key, fast even for large dictionaries
joel_has_grade = "Joel" in grades   # True
kate_has_grade = "Kate" in grades   # False
print("{1}, {0}".format(joel_has_grade, kate_has_grade))

# recommended to use get method, as handles better keys not present
joels_grade = grades.get("Joel", 0)     # equals 80
kates_grade = grades.get("Kate", 0)     # equals 0
no_ones_grade = grades.get("No One")    # default is None
print(f"{joels_grade}, {kates_grade}, {no_ones_grade}")

# assing key/value pairs
grades["Kate"] = 100        # adds a third entry
grades["Adolf"] = 97        # replaces/modifies the old value
num_students = len(grades)  # equals 3
print(f"{num_students}, {grades['Adolf']}, {grades['Kate']}")

# dictionaries to represent structured data
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
print(tweet)
# can look at all the keys
tweet_keys = tweet.keys()       # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items = tweet.items()     # iterable for the (key, value) tuples

print("user" in tweet_keys)            # True, but not Pythonic
print("user" in tweet)                 # Pythonic way of checking for keys
print("joelgrus" in tweet_values)      # True (slow but the only way to check)

# defaultdict