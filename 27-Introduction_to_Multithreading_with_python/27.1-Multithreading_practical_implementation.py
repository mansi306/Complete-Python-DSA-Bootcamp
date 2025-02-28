'''
Multithreading
When to use Multi Threading :
1) I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
2) Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.
'''
import threading
import time 

def print_number():
    for i in range(5):
        time.sleep(1)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")


##create 2 threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)


t=time.time()
## start the thread
t1.start()
t2.start()

### Wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)


#  Single-threaded Program (Runs Sequentially)
'''
import time
def task():
    for i in range(3):
        time.sleep(1)
        print(f"Task {i}")
task()
task()
'''

# Multi-threaded Program (Runs Simultaneously)
'''
import threading
import time

def task():
    for i in range(3):
        time.sleep(1)
        print(f"Task {i}")

# Creating two threads
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

'''
