import time
from multiprocessing import Pool, cpu_count
import os

def heavy_compute(n):
    # simulate CPU heavy work (some compute)
    s = 0
    for i in range(10_00_00_000):
        s += (i * i) % (n + 1)
    return s

if __name__ == "__main__":
    inputs = [1,2,3,4,5,6,7,8]  # 8 tasks
    start = time.perf_counter()
    # sequential
    results = [heavy_compute(x) for x in inputs]
    print("Sequential time:", time.perf_counter() - start)

    start = time.perf_counter()
    # Use the number of available CPU cores for optimal performance
    num_processes = cpu_count()
    print(f"Number of processes being used: {num_processes}")
    with Pool(processes=8) as p:
        results = p.map(heavy_compute, inputs)
    print("Multiprocessing time:", time.perf_counter() - start)
