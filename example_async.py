import asyncio
import time


def prime_generator():
    n: int = 2
    primes: set = set()

    while True:
        test = [p for p in primes if n % p == 0]
        if not any(test):
            primes.add(n)
            yield n
        n += 1


async def prime_factors(n):
    print(f'Starting processing for {n}')
    factors = {}
    primes = prime_generator()
    v = n
    for p in primes:
        if v <= 1:
            break
        while v > 1 and v % p == 0:
            if p not in factors:
                factors[p] = 1
            else:
                factors[p] += 1
            v /= p
        await asyncio.sleep(0)
    print(f'Finished processing for {n}')
    return factors


async def process_value(n):
    factors = await prime_factors(n)
    print(f'>> Factors of {n}: {factors}')


def main():
    start = time.clock()

    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

    task = asyncio.gather(
        process_value(223976),
        process_value(1042751),
        process_value(1209429),
        process_value(3939039),
        process_value(5380794)
    )

    loop.run_until_complete(task)
    loop.close()

    end = time.clock()
    print(f'Time taken: {end - start} seconds')


if __name__ == '__main__':
    main()
