# importing modules
import re
my_regex = re.compile("[0-9]+", re.I)

# if already imported re then may use an alias
# or if the module has an unwieldy name e.g., matplotlib.pyplot as plt
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# Here we go -> Feb 2025 FSQ
import re
my_regex = re.compile("[0-9]+", re.I)

import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# if I were a bad person, I would import entire contents of a module
# as follows.
match = 10
from re import * # uh oh, re has a match function
print(match)    # "<function match at 0x10281e6a8>"
#  However, since I am not a bad person, I won't ever do this.

