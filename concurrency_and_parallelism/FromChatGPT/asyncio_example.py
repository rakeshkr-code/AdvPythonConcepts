# asyncio_example.py
import asyncio
import time

async def io_task(name, delay):
    print(f"[{time.strftime('%X')}] {name} started, sleeping {delay}s")
    await asyncio.sleep(delay)
    print(f"[{time.strftime('%X')}] {name} finished")

async def main():
    start = time.perf_counter()
    # schedule 5 tasks concurrently
    tasks = [asyncio.create_task(io_task(f"task-{i}", 1)) for i in range(5)]
    await asyncio.gather(*tasks)
    print("Asyncio total time:", time.perf_counter() - start)

if __name__ == "__main__":
    asyncio.run(main())
