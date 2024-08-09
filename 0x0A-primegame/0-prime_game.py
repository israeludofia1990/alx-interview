#!/usr/bin/python3
'''Prime Game'''


def sieve(n):
    '''
    Return a list of primes up to
    n using the Sieve of Eratosthenes
    '''
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    '''
    determines the winner of a game using
    Sieve of Eratosthenes algorithm
    '''
    if x <= 0:
        return None
    max_num = max(nums) if nums else 0
    prime_numbers = sieve(max_num)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if n >= 2:
            count = sum(1 for p in prime_numbers if p <= n)
            if count % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1
        elif n == 1:
            ben_wins += 1
        else:
            pass
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
