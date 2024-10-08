# logical operator: one that evaluates to multiple conditions
# or : at least one condition must be TRUE
# and: both the conditions must be TRUE
# not: Inverts the condition (Not FALSE, Not TRUE)

temp = 25
is_raining = True

if temp < 18 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The OutDoor event is as per the schedule")

###Using and condition
temp = 30
is_sunny = True
if temp >= 28 and is_sunny:
    print("Its Hot outside " + "☀️☀️☀️☀️☀️") # WindowsKey + .
    print("Its really Sunny ♨️")

## Todo: Try an example of not operation.
