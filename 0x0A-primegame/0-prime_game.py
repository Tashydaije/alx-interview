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

    # Create a set of primes for quick lookup
    prime_set = set(primes)

    def count_prime_moves(n):
        """Count the number of moves possible for a given n"""
        moves = 0
        visited = set()
        for num in range(2, n + 1):
            if num not in visited and num in prime_set:
                moves += 1
                for multiple in range(num, n + 1, num):
                    visited.add(multiple)
        return moves

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_prime_moves(n)
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
