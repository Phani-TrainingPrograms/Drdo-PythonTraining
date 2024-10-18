# dictionary collection of {key:value} pairs which is ordered and unchangeable. U cannot have duplicates in terms of keys:
capitals = { "USA" : "Washington D.C.", "India" : "New Delhi", "China" : "Beijing", "Japan" : "Tokyo" }

###########Adding pair to the dictionary###################
capitals.update({"Germany" : "Berlin"})
capitals["Canada"] = "Ottawa"
capitals["India"] = "Bhopal" #Updating the record.

capitals.pop("China")
print(capitals)

keys = capitals.keys()
# values = capitals.values()
for key in keys:
    print(f"Country: {key}, Captial: {capitals[key]}")
print("#######################################################")
for key, value in capitals.items():
    print(f"Country: {key}, Captial: {value}")


# Exercise 1: Create a data for an employee: An object could be a dictionary where its attributes are keys and their associated values are their value for each of those keys
employee = {}
employee["id"] = 123
employee["name"] = "Phaniraj"
employee["address"] = "RR Nagar, Bangalore"
employee["salary"] = 45000

print("These are the details of the Employee: ")
for key, value in employee.items():
    print(f"{key} : {value}")