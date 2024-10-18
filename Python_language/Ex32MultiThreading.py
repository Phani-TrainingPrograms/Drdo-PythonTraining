# What is a process?
# A process is a running instance of an executable. A process maintains a private address space
# within which its code, binaries are loaded and executed.

# What is a thread?
# A thread is a part of a process that defines the path of execution. Most of the Apps have an
# entry point from which the app execution begins. This function would be invoked as soon as the
# process starts. Internally, a thread gets created within the process and the thread shall
# associate itself with this function and starts executing it. When this function ends,
# the thread shall terminate and close. Once no threads are executing, the process kills itself.
# The thread that starts when the process begins is called as Main thread or UI Thread.
# Usually apps work well with single threads or UI threads. But for certain scenarios, when the
# main thread is blocked for very long operation, U can make such operations execute in a
# separate path of execution and allow the main thread to do its tasks parallel.
# Why U need multi Threading?
# If a task takes a longer duration to complete its work, then U dont want other tasks to wait
# for its completion. Instead, U can create a new thread for such tasks and allow them to run
# while UR Main thread continues its execution. Practical examples: Lift management software.
# IDEs uses threads to manage multiple windows.
# How to create Multi threading code
# In Python, U use threading module to create multi-threading apps. Your OS should support multithreading if U want to implement threading in ur code.
# Issues with multi threading:
# As threads are executed parallel, if both the threads are trying to use the same resource,  it might lead to data corruption.
import threading
import time

def downloading_file(filename, duration):
    print(f"Starting download for {filename}...")
    for i in range(1 , duration + 1):
        print("Downloading file....")
        time.sleep(1)
    print(f"Finished downloading {filename}")

def process_data(data, duration):
    print(f"Starting to process {data}")
    for i in range(1, duration + 1):
        print(f"Processing data {data}....")
        time.sleep(1)
    print(f"Finished processing {data}")

#create threads:
thread1 = threading.Thread(target=downloading_file, args=('file1.zip', 5))
thread2 = threading.Thread(target=process_data, args=('data1', 10))

# print("Main program is running now............")
# #start the threads where they shall execute parellelly
# thread1.start()
# thread2.start()
#
# print("Main Program is continuing to do the job")
# for i in range(1, 10):
#     print("Main doing its job")
#     time.sleep(1)
#
# # Allow the main program to wait till all the threads are completed.
# thread1.join()
# thread2.join()
#
# print("All the threads are done with the job")

#########################Using locks##########################################
# Shared resource:
counter  = 0
# Lock for the resource
lock = threading.Lock()

def increment_counter(arg):
    lock.acquire()
    global counter
    for _ in range(10):
        time.sleep(1)
        counter += 1
        print(f"counter: {counter} from thread {arg}")
    lock.release()

t1 = threading.Thread(target=increment_counter, args=("1"))
t2 = threading.Thread(target=increment_counter, args=("2"))

t1.start()
t2.start()

t1.join()
t2.join()
print(f"Final counter value: {counter}" )