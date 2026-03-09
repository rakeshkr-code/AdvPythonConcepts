"""
This script compares the execution time of three approaches to handle I/O-bound tasks in Python: Sequential, Multithreading, and Multiprocessing. 
Each task simulates an I/O operation by sleeping for a specified duration. The script demonstrates how multithreading can significantly reduce the execution time for I/O-bound tasks, while multiprocessing may not provide the same benefits due to the overhead of process creation and inter-process communication.
"""
import os
import time
import threading
import multiprocessing

def io_worker(id, delay):
    print(f"Task [{id}] sending network request (waiting {delay}s)...")
    # time.sleep() simulates an I/O-bound operation, like waiting for an API response.
    # During this time, the Python GIL is released!
    time.sleep(delay) 
    print(f"Task [{id}] received response!")
    return True

if __name__ == "__main__":
    # Number of tasks and simulated wait time per task
    num_tasks = 20
    wait_time = 1 

    print(f"Running {num_tasks} I/O-bound tasks, simulating a {wait_time} second wait each.")
    print(f"Number of CPU cores available: {os.cpu_count()}\n")

    # 1. Timing the Sequential approach
    print("--- Starting Sequential ---")
    wall_start_time = time.perf_counter()
    cpu_start_time = time.process_time()
    for i in range(num_tasks):
        io_worker(i, wait_time)
    wall_end_time = time.perf_counter()
    cpu_end_time = time.process_time()
    print(f"Sequential completed in {wall_end_time - wall_start_time:.2f} seconds (CPU time: {cpu_end_time - cpu_start_time:.2f} seconds).\n")

    # 2. Timing the Multithreading approach
    print("--- Starting Multithreading ---")
    start_time = time.perf_counter()
    threads = []
    for i in range(num_tasks):
        t = threading.Thread(target=io_worker, args=(i, wait_time))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()  
    end_time = time.perf_counter()
    print(f"Multithreading completed in {end_time - start_time:.2f} seconds.\n")

    # 3. Timing the Multiprocessing approach
    print("--- Starting Multiprocessing ---")
    start_time = time.perf_counter()
    processes = []
    for i in range(num_tasks):
        p = multiprocessing.Process(target=io_worker, args=(i, wait_time))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()  
    end_time = time.perf_counter()
    print(f"Multiprocessing completed in {end_time - start_time:.2f} seconds.\n")
