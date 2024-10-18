# DateTime module in python contains classes for working with Date and Time. With these APIs, U
# can perform operations on Date and Time like extracting the System Date and Time, performing
# mathematical operations on Date and Time.
import datetime as dt
from datetime import datetime

#current datetime:
now = dt.datetime.now()
print("Current Date and time is " + str(now))

#current time:
time = now.strftime("%H: %M: %S")
print(time)

time = f"{now.time().hour} : {now.time().minute} : {now.time().second}"
print(time)

# current Date:
# date = dt.datetime.today()
date = now.strftime("%Y-%m-%d")
print(f"Today's Date is {date}")

# How about taking inputs from the user?
#dob = input("Enter the Date of birth as %Y-%m-%d")
#date_of_birth = dt.datetime.strptime(dob, "%Y-%m-%d")
#print(f"UR Date of Birth is {date_of_birth}" )

#Todo: Calculate the age based on the date of birth:
def calculate_age(dateofbirth):
    today = dt.datetime.today()
    age = today.year - dateofbirth.year
    if(today.month, today.day) < (dateofbirth.month, dateofbirth.day):
        age -= 1
    return age

dob = dt.datetime(1976, 12, 1)
age = calculate_age(dob)
print(age)

#Adding date
my_retirement_year = now.year + 4
print(f"The selected year is {my_retirement_year}")

# Adding days:
my_retirement_date = now + dt.timedelta(days= 1000)
print(f"The selected date is {my_retirement_date}")

#Subtract the days:
old_date = dt.date(2002, 12,4)
previous_visit = now - dt.timedelta(days = -456)
diff = dt.datetime.now().date() - old_date
print(f"No of days: {diff.days}")

########################Important points#################################
'''
datetime.datetime.now : Gets the system date and time. 
datetime.datetime.today : returns the current system date
strftime() is used for formatting the date time
strptime() is used to parse the string to a valid datetime
timedelta() is used to add/subtract dates.

Weekly format for modelling analysis. 
Aggregation
'''

