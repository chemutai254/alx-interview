#!/usr/bin/python3
"""Prime game - the game determines the winner"""


def primeNum(n):
    """
    Returns prime numbers
    """
    prime = []
    bound = [True] * (n + 1)
    for a in range(2, n + 1):
        if (bound[a]):
            prime.append(p)
            for b in range(a, n + 1, a):
                bound[b] = False
    return prime


def isWinner(x, nums):
    """
    Args:
    x: number of rounds
    nums: array of n
    returns the name of the player that won the most rounds
    returns: None id the winner cannot be determined
    """

    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primeNum(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
        if Maria > Ben:
            return 'Maria'
        elif Ben > Maria:
            return 'Ben'
        else:
            return None
