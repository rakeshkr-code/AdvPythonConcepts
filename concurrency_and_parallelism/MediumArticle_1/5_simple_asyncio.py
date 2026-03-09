import asyncio
from time import time

async def task(name):
    print(f"Task {name} starting")
    await asyncio.sleep(5)  # Simulate an I/O-bound operation
    print(f"Task {name} finished")
# time
start_time = time()
async def main():
    await asyncio.gather(task("A"), task("B"), task("C"))

asyncio.run(main())
end_time = time()

print(f"All tasks completed in {end_time - start_time:.2f} seconds")