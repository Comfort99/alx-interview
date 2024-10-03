#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ x - rounds
        nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    boy = 0
    girl = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            boy += 1
        else:
            girl += 1
    if boy > girl:
        return "Ben"
    if girl > boy:
        return "Maria"
    return None


def rm_multiples(lst, x):
    """ removes multiple of primes """
    for i in range(2, len(lst)):
        try:
            lst[i * x] = 0
        except (ValueError, IndexError):
            break
