from statistics import median

import numpy as np
from scipy import  stats


# numpy is a python library for performing numerical calculations in python.
# arrays are the most optimized collection components. Its fixed in size and once the memory is set, U can use it to perform various kinds of operations.
def perform_array_operations(arr):
    print(arr)
    print(type(arr))
    print(arr.shape)
    #Shape property gives a tuple of integers representing size and no of elements in that
    # dimensions.
    # describes about the array like no of dimensions and count of each dimension.

# How to create a 1-D Array using numpy:
# arr1 = np.array([1,2,3,4,5, 6,7,8,9])
# mul_arr = np.array([[1,2,3,4,5, 6,7,8,9], [1,2,3,4,5, 6,7,8,9]])
# print("####################For Single Dimensional Array###########################")
# perform_array_operations(arr1)
# print("####################For Multi Dimensional Array###########################")
# perform_array_operations(mul_arr)
# print("####################Creating Multi-Dimensional Array###########################")
# mul_arr = np.array([1,2,3,4,5], ndmin= 3)
# perform_array_operations(mul_arr)
print("####################Arrays of values###########################")
# ones = np.ones((2,4)) #2x4 array with values set to 1.
# print(ones)
#
# # Create array with range of values with start, end and step.
# range_arr = np.arange(10, 30, 2)
# print(range_arr)
#
# rand_arr = np.random.rand(4, 5)
# print(rand_arr* 10) # random gives a random value b/w 0 and 1.

#Important properties: ndim, size, dtype, itemsize.
def print_info_array(arr):
    print("Array: \n", arr)
    print("Shape: \n", arr.shape)
    print("No of dimensions: ", arr.ndim)
    print("Size(No of elements): ", arr.size)
    print("Data Type: ", arr.dtype)
    print("Item Size: (Byte size)", arr.itemsize) # What does size of an item mean?

# arr = np.array([[1,2,3,4,5], [5,6,7,8,9]])
# print_info_array(arr)

##############################Indexing feature of arrays################################
# arr = [1,2,3,4,5,6,7,8,9,10]
# single_element = arr[1]
# print(single_element)
# firt_three_elements = arr[1:4] #Gets from 1 to 4 excluding 4. This concept is called as SLICING.
# print(firt_three_elements)
# print(arr[-2])
#
# print(arr[:5]) #Starts with 0 till 4
# print(arr[::2])#Displays all elements from 0 to end stepping 2.
# print(arr[::-1])# reverse display of array
# print(arr[-4:-8:-2])
#
# sqr_arr = [x**2 for x in arr] # Exponential multiplication of every index.
# print(sqr_arr)
#####################################Vector operations########################
# arr1 = np.array([1,2,3,4,5])
# arr2 = arr1 * 10

# print(f"Addition: ", arr1 + arr2)
# print(f"Subtract: ", arr1 - arr2)
# print(f"Multiply: ", arr1 * arr2)
# print(f"Divide: ", arr1 / arr2)

############################Common Global functions#####################
# print(np.sqrt(arr1))
#
# print(np.sin(arr1))
#
# print(np.log(arr1))
#
# print(arr1[(arr1 >=3) & (arr1 <= 10)])

########################Statistical functions#########################
# arr1 = np.array([1,2,3,4,5])
# mean = np.mean(arr1)
# median_value = np.median(arr1)
# std_deviation = np.std(arr1)
# variance = np.var(arr1)
# mode_value = stats.mode(arr1)
#
#
# print(f"Mean: ", mean)
# print("Median: ", median_value)
# print("Standard Deviation: ", std_deviation) #standard measure of how data is clustered around the mean
# print("Variance: ", variance) #The mean of the squares subtracted by the square of the mean
# print("Mode: ", mode_value)

############################Sorting function##########################
# arr1 = np.array([3,4,2,5,1,6,9,8])
# sorted_arr = np.sort(arr1) # [::-1]
# sorted_indices = np.argsort(arr1) #Sorting the values and return the indices.
# print(sorted_arr, sorted_indices)

#################Unique values##############################
arr1 = np.array([3,4,5,6,7,5,4,7,8])
unique_values = np.unique(arr1)
#unique_counts = np.unique(arr1, return_counts=True)
values, count = np.unique(arr1, return_counts=True)

print("Unique values: ", unique_values)
#print("Unique Counts: ", unique_counts)

# Histogram
for value, count in zip(values, count):
    print(f"Value {value} appears {count} no of times")


