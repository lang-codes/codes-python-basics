# Describes simple usage of the time module using one function

import time
import asyncio

# Defining timer function to check for time lapse
async def timer():
    s = time.perf_counter()
    await asyncio.sleep(2)
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

asyncio.run(timer())
