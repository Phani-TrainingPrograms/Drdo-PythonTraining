# sets: unordered and immutable collections but can hold only unique values in it. It can allow to add and remove the items from it.
# sets are created using {} braces.
names = { "Phani", "Vinod", "Banu", "Ramnath", "JoyDip", "Phani" }
print(names)
print(names)
# prints the values in unordered manner.
for name in names:
    print(name)

# print(names[1]) # As the Sets are unordered, U cannot use indexing to the collection. U cannot
# alter the items in the set, however, U can add/remove items from the set.

names.add("Murali")
print(names)

# Adding bulk records:
trainers = {"Krishna", "Nathan", "Somnath"} # Adding another set into the current set.
names.update(trainers)
print(names)

# Removing items from the set:
# remove and discard function: remove throws an error if an item is not found to remove from the set, but discard shall not throw any exception.
# How many ways can we remove items in collection: 4 ways: remove, discard, pop and clear.
names.add("Phani")


