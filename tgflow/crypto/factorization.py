import math
import random


def factorize_pq(pq: int) -> tuple[int, int]:
    if pq % 2 == 0:
        p, q = 2, pq // 2
        return (p, q) if p <= q else (q, p)

    y = random.randint(1, pq - 1)
    c = random.randint(1, pq - 1)
    m = random.randint(1, pq - 1)
    g = 1
    r = 1
    q = 1

    while g == 1:
        x = y
        for _ in range(r):
            y = (pow(y, 2, pq) + c) % pq

        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = (pow(y, 2, pq) + c) % pq
                q = (q * abs(x - y)) % pq

            g = math.gcd(q, pq)
            k += m
        r *= 2

    if g == pq:
        while True:
            ys = (pow(ys, 2, pq) + c) % pq
            g = math.gcd(abs(x - ys), pq)
            if g > 1:
                break

    p = g
    other = pq // p
    return (p, other) if p <= other else (other, p)
