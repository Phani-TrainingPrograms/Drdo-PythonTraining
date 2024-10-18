# Plots Example
# Understand how to create graphs in python.

import matplotlib.pyplot as plt # Graphs
import pandas as pd #Data analysis
import numpy as np #Numerical calculations.

# plt.figure(figsize=(8,5), dpi=100)
# x = [0, 1,2,3,4,5]
# y= [0,2,4,6,8,10]
# x2 = [1, 2, 3]
# x3 = [1, 4, 9]
# # plt.plot(x, y, label="2x", color="b", marker=".", linestyle="--")
# # format of shortcut: [color][marker][linestyle]
# plt.plot(x, y, 'y*--')
# plt.plot(x2, x3, 'b', label='x^2')
# plt.xlabel("Units")
# plt.ylabel("2 x Units")
# plt.title("Multiplier")
# plt.xticks(x)
# plt.yticks(y)
# plt.legend()
#
# plt.savefig('basic.png', dpi=300)
# plt.show()

######################################Pie Charts#########################################
# marital_status = ['Married', 'Single', 'Unknown']
# values = [40, 30, 30]
# colors = ['green', 'lightcoral', 'grey']
# plt.pie(values, labels=marital_status, colors=colors, autopct='%1.1f%%')
# plt.title('Customers Marital Status')
# plt.show()

#####################################Bar Graphs###########################################
labels = ['A', 'B', 'C']
values = [1,4,6]
plt.figure(figsize=(5,3), dpi = 100) # For saving files.
bars = plt.bar(labels, values)

patterns = ['/', 'o', '*']
for bar in bars:
    bar.set_hatch(patterns.pop())


plt.savefig('barchart.png', dpi=300)
plt.show()
###########################################################################
