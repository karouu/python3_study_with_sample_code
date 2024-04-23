#!/usr/bin/env python3
# rand.py

import asyncio
import random

# colors
c = (
    "\033[0m",   # end of color
    "\033[36m",  # cyan
    "\033[91m",  # red
    "\033[35m",  # magenta
)

'''
async randint function is not necessary to be asynchronous since it simply delegates the task to 
the random.randint function, which is synchronous. 
In this case, making randint asynchronous doesn't provide any additional benefits.'''
async def randint(a: int, b: int) -> int:
    return random.randint(a, b)


async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx + 1] + f"Initiated makerandom({idx}).")
    # guess = await randint(0, 10)
    guess = random.randint(0, 10)
    while guess <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {guess} too low; retrying.")
        await asyncio.sleep(idx*1.5 + 1)
        guess = await randint(0, 10)

    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {guess}" + c[0])
    return guess


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
