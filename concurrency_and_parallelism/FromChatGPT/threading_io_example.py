# threading_io_example.py
import threading
import time

def io_task(name, delay):
    print(f"[{time.strftime('%X')}] {name} started, sleeping {delay}s")
    time.sleep(delay)
    print(f"[{time.strftime('%X')}] {name} finished")

def run_sequential():
    start = time.perf_counter()
    for i in range(5):
        io_task(f"task-{i}", 1)
    print("Sequential time:", time.perf_counter() - start)

def run_threaded():
    start = time.perf_counter()
    threads = []
    for i in range(5):
        t = threading.Thread(target=io_task, args=(f"task-{i}", 1))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("Threaded time:", time.perf_counter() - start)

if __name__ == "__main__":
    run_sequential()
    run_threaded()
