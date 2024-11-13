# working with strings
single_quoted_string = 'data science'
double_quoted_string = "data science"
print ("single=", single_quoted_string, "and double=", double_quoted_string)

tab_string = "\t"       # represents the tab character
print(len(tab_string))  # is 1

# creating raw string using r""
not_tab_string = r"\t"      # represents the characters '\' and 't'
print(len(not_tab_string))  # is 2

# multiline strings
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
print(multi_line_string)

# f-string to conveniently combine two or more strings and most preferred
first_name = "Adolf"
last_name = "Rutebeka"

full_name1 = first_name + " " + last_name               # string addition
full_name2 = "{1} {0}".format(first_name, last_name)    # string.format
full_name3 = f"{first_name} {last_name}"
print("{0}, {1}, {2}".format(full_name1, full_name2, full_name3))


