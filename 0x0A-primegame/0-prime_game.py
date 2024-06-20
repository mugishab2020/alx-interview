#!/usr/bin/python3
'''this is the function that returns the winner of teh prime game'''


def isWinner(x, nums):
    '''Prime Game'''
    if x <= 0 or not nums:
        return None
    e_cache_primes = {}
    wins = {"Maria": 0, "Ben": 0}
    for i in range(x):
        query_num = nums[i]
        if query_num in e_cache_primes:
            count = e_cache_primes[query_num]
        else:
            # counting primes using Sieve of Eratosthenes algorithm
            primes = [True for _ in range(query_num + 1)]
            p = 2
            while p * p <= query_num:
                if primes[p]:
                    for x in range(p * p, query_num + 1, p):
                        primes[x] = False
                p += 1
            count = 0
            for i in range(query_num + 1):
                if primes[i]:
                    count += 1
            e_cache_primes[query_num] = count
        if count % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1
    if wins['Maria'] == wins['Ben']:
        return None
    return 'Maria' if wins['Maria'] > wins['Ben'] else 'Ben'
