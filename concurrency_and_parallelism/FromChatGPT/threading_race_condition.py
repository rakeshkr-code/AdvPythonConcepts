# # threading_race_condition.py
# import threading
# import time

# counter = 0
# lock = threading.Lock()

# def worker(n):
#     global counter
#     for _ in range(n):
#         # without lock -> race condition
#         # counter += 1
#         with lock:
#             counter += 1

# if __name__ == "__main__":
#     threads = [threading.Thread(target=worker, args=(100_00_000,)) for _ in range(4)]
#     for t in threads: t.start()
#     for t in threads: t.join()
#     print("Counter:", counter)  # should be 4*100000


# ----------------------------------------------------------

# sequential_vs_threading.py
import threading
import time

counter = 0
lock = threading.Lock()

N = 10_000_000
NUM_THREADS = 4


def worker(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1


def run_sequential():
    global counter
    counter = 0

    start = time.perf_counter()

    for _ in range(NUM_THREADS):
        worker(N)

    end = time.perf_counter()

    print("Sequential Counter:", counter)
    print("Sequential Time:", end - start)


def run_threading():
    global counter
    counter = 0

    threads = [threading.Thread(target=worker, args=(N,)) for _ in range(NUM_THREADS)]

    start = time.perf_counter()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()

    print("Threading Counter:", counter)
    print("Threading Time:", end - start)


if __name__ == "__main__":
    print("Running Sequential...")
    run_sequential()

    print("\nRunning Threading...")
    run_threading()