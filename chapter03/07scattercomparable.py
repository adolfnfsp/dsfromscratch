"""
Scattering comparable variables, might get a misleading
picture if you let matplotlib choose the scale
"""

from matplotlib import pyplot as plt

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
# plt.axis("equal") # makes scatterplot with equal axes
plt.show()
