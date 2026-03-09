"""
Multiprocessing vs Multithreading in Python: A Comprehensive Comparison
This article explores the differences between multiprocessing and multithreading in Python, highlighting their use cases, advantages, and limitations. 
Here two approaches are implemented for a "CPU-bound" or "CPU-heavy" task to demonstrate their performance differences.
Conclusion:
- Multiprocessing is ideal for CPU-bound tasks as it can utilize multiple CPU cores
- But multithreading will not be effective for CPU-bound tasks due to the Global Interpreter Lock (GIL) in Python, which allows only one thread to execute Python bytecode at a time.
- Here, threading will take similar time as sequential execution, while multiprocessing can significantly reduce the execution time by leveraging multiple CPU cores.
"""
import os
import time
import threading
import multiprocessing

def worker(id, num):
    print(f"Worker [{id}] starting with number {num}...")
    # simulate CPU heavy work (some compute)
    s = 0
    for i in range(num):
        s += (i * i)
    print(f"Worker [{id}] finished with result {s} !")
    return s

if __name__ == "__main__":
    # Number of tasks and workload
    num_tasks = 4
    workload = 10_00_00_000

    print(f"Running with {num_tasks} tasks and workload of {workload} iterations each.")
    print(f"Number of CPU cores available: {os.cpu_count()}")

    # Timing the multiprocessing approach
    start_time = time.perf_counter()
    processes = []
    for i in range(num_tasks):
        p = multiprocessing.Process(target=worker, args=(i, workload))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()  # Wait for all processes to finish
    end_time = time.perf_counter()
    print(f"Multiprocessing completed in {end_time - start_time:.2f} seconds.")

    # Timing the multithreading approach
    start_time = time.perf_counter()
    threads = []
    for i in range(num_tasks):
        t = threading.Thread(target=worker, args=(i, workload))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()  # Wait for all threads to finish
    end_time = time.perf_counter()
    print(f"Multithreading completed in {end_time - start_time:.2f} seconds.")

    # Timing the sequential approach
    # Along with perf counter, compare wall time vs CPU time and print both
    wall_start_time = time.perf_counter()
    cpu_start_time = time.process_time()
    for i in range(num_tasks):
        worker(i, workload)
    wall_end_time = time.perf_counter()
    cpu_end_time = time.process_time()
    print(f"Sequential execution completed in {wall_end_time - wall_start_time:.2f} seconds (CPU time: {cpu_end_time - cpu_start_time:.2f} seconds).")
