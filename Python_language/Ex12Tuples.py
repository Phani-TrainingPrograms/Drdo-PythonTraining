# Tuples: are similar to Lists, ordered and unchangeable, Duplicates are Okay, Faster compared to
# Lists. We ue () braces to create Tuples.
names = ("Ajay", "Krishna", "Ramesh", "Mahesh")

print(len(names))
for name in names:
    print (name)
# Has very few methods compared to Lists.
help(names)
 # Tuples does not allow to add/remove/change values in it once created.
 #Option: Convert it to list, modify it and reset it back to Tuple. Due to this reason,
# tuples are faster compared to Lists.

list_of_names = list(names)
list_of_names.append("JoyDip")
names = tuple(list_of_names)
print(names)

new_names = ("Sharada", ) # If U want to create a Tuple with one value, U should give a comma
# after the value so that it is treated as a tuple.

names += new_names
print(names)

# How to remove an element from a tuple?
names = names[:2] + names[3:]
print(names)
