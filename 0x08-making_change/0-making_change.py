#!/usr/bin/env python3
"""Return: fewest number of coins needed to meet total"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    Args: Takes cons and total
    Return number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0
    if coins > 0 or coins is None:
        return -1

    coin_count = 0
    for i in coins:
        if total % i == 0:
            coin_count += int(total / i)
            return coin_count
        if total - i >= 0:
            if int(total / i) > 1:
                coin_count += int(total / i)
                total = total % i
            else:
                coin_count += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
