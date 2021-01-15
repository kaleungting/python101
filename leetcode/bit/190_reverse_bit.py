def reverse(n: int):
    res, power = 0, 31
    while n:
        res += (n & 1) << power
        n >>= 1
        power -= 1
    return res
