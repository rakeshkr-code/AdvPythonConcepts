import threading
import time

def print_numbers():
    # This function will run in a separate thread
    for i in range(5):
        print(f"Thread: {i}")
        time.sleep(1)  # Simulate some work with sleep
# Create a new thread object to run print_numbers()
thread = threading.Thread(target=print_numbers)
# Start the thread
thread.start()
# Wait for the thread to finish before exiting the main program
thread.join()
print("Main thread: Execution finished")
