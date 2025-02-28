'''
Processes that run in parallel
1) CPU-Bound Tasks - Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing)
2) Parallel execution - Multiple cores of the CPU
'''
import multiprocessing
import time 

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

if __name__=="__main__":
    
    ## create 2 processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    ## start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)



'''
import multiprocessing
import time

def process_task(name):
    print(f"Process {name} started")
    time.sleep(2)
    print(f"Process {name} finished")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=process_task, args=("A",))
    p2 = multiprocessing.Process(target=process_task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both processes are done!")

'''
