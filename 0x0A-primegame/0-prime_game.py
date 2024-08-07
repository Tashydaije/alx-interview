#!/usr/bin/python3

"""solving a prime game scenarion"""


def sieve(n):
    """sieve of eratosthenes: generates a list of all prime numbers
    up to max no. of input"""
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    """handles game simulation and winner determination"""
    if not nums or x <= 0:
        return None
    
    max_num = max(nums)
    primes = sieve(max_num)
    
    # DP array to count the number of prime removals up to each number
    prime_counts = [0] * (max_num + 1)
    
    for prime in primes:
        for multiple in range(prime, max_num + 1, prime):
            prime_counts[multiple] += 1
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
