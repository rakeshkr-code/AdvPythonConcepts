import multiprocessing
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)  # Simulate some work
    print(f"Worker {name} finished")
if __name__ == '__main__':
    # time
    start_time = time.time()
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()  # Wait for all processes to finish
    end_time = time.time()
    print(f"Main process: All workers finished in {end_time - start_time} seconds")