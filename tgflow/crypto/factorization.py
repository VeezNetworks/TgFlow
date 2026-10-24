import math


def factorize(pq: int) -> tuple[int, int]:
    if pq % 2 == 0:
        return 2, pq // 2
    for i in range(3, 1000, 2):
        if pq % i == 0:
            return min(i, pq // i), max(i, pq // i)
    x = 2
    y = 2
    d = 1
    c = 1
    while d == 1:
        x = (pow(x, 2, pq) + c) % pq
        y = (pow(y, 2, pq) + c) % pq
        y = (pow(y, 2, pq) + c) % pq
        d = math.gcd(abs(x - y), pq)
        if d == pq:
            x += 1
            y = x
            c += 1
            d = 1
    return min(d, pq // d), max(d, pq // d)
