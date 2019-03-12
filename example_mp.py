import time
from multiprocessing import Pool


def prime_generator():
    n: int = 2
    primes: set = set()

    while True:
        test = [p for p in primes if n % p == 0]
        if not any(test):
            primes.add(n)
            yield n
        n += 1


def prime_factors(n):
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
    print(f'Finished processing for {n}')
    return factors


def process_value(n):
    print(f'>> Factors of {n}: {prime_factors(n)}')


def main():
    start = time.clock()

    with Pool(6) as pool:
        pool.map(process_value, [223976, 1042751, 1209429, 3939039, 5380794])

    end = time.clock()
    print(f'Time taken: {end - start} seconds')


if __name__ == '__main__':
    main()
