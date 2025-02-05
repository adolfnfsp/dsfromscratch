# Strings
single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = "\t"       # represents the tab character
len(tab_string)         # is 1

# raw strings using r
not_tab_string = r"\t"  # represents the character '\' and 't'
len(not_tab_string)     # is 2

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

# the f-string
first_name = "Joel"
last_name = "Grus"
full_name1 = first_name + " " + last_name             # string addition
full_name2 = "{0} {1}".format(first_name, last_name)  # string.format
full_name3 = f"{first_name} {last_name}"              # with f-string, preferred way

