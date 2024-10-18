# Python does not have the concept of arrays.
# Lists are the way of storing large amount of data and represent them as a single unit. U refer
# each element inside it by index operator []
# Lists = ordered, changable and U can have duplicates.

fruits = ["Apple", "Mango", "Orange"]
# print(fruits)
# print(fruits[0]) # Indexing is a way to refer each item in the List. it starts from 0.
# print(fruits[1])
# print(fruits[2])

# for fruit in fruits:
#     print(fruit)

# print(f"The no of fruits in our basket is {len(fruits)}")
# print("pineapple" in fruits) # false
# print(dir(fruits))
#help(fruits)

fruits.append("pineapple") # Adds the element to the bottom of the list.
print("pineapple" in fruits) # true
fruits.insert(0, "Guava")
fruits.insert(3, "Kiwi Fruit")

# Try to remove an item from the fruits
# fruits.remove("pineapple")
# fruits.sort() # Sorts the element
#
# print(fruits)
# print(fruits[-1]) # Use -ve index to get the last item
# print(fruits[2:5]) # Returns 3rd, 4th and 5th item. Starts from index 2(included) and ends at
# # index 5(excluded)
# print(fruits[:3]) # From the start index to the 3rd index (excluding)
# print(fruits[2:]) # From the 2nd index till the last
print(fruits)
##############Modifying the contents of the List#############################
fruits[1:3] = ["watermelon", "Dragon Fruit", "Pomegranate", 123] # Modifies the elements at index 1
# and 2
print(fruits)
# If U insert more items than what U intend to replace, the new items will be inserted from the
# location where U have specified.


