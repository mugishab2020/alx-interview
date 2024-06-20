#!/usr/bin/python3
'''this is the function that returns the winner of teh prime game'''


def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n == 2 or n == 3:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        prime_count = 0
        for num in range(1, n + 1):
            if is_prime(num):
                prime_count += 1
        if prime_count % 2 == 1:
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1

    if wins["Maria"] == wins["Ben"]:
        return None
    return "Maria" if wins["Maria"] > wins["Ben"] else "Ben"
