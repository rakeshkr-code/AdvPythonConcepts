import threading
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)  # Simulating I/O-bound work
    print(f"Worker {name} finished")
threads = []
start_time = time.time()
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
    # worker(i)  # Running worker in the main thread for demonstration
for t in threads:
    t.join()  # Wait for all threads to complete
end_time = time.time()
print(f"Total time: {end_time - start_time}")
