# The OS module is used to extract information from the OS where the Application is executing
# It allows to perform tasks on File and Directory management, environment variables and process
# information.

import os
# Get the Current working directory
current_dir = os.getcwd()
print(f"The Current working is {current_dir}")

all_details = os.listdir(current_dir)
for file in all_details:
    print(f"File Name: {file}")

# Use Environment variables:
path_var = os.environ.get('PATH')
print("Environment variables for Path: ", path_var)

#Check if the directory exists:
if os.path.exists(current_dir):
   print("This directory exists")
else:
    os.mkdir(current_dir)
    print(f"A new directory {current_dir} is now created")

# Get the List of available Drives in the OS:
drives = os.listdrives()
for dr in drives:
    print(dr)






