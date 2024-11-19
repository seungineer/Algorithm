import math
mod = int(1e9+7)

def f(num, exp):
    if exp == 1:
        return num
    if exp % 2 == 0:
        half = f(num, exp//2)
        return half * half % mod
    else:
        return num * f(num, exp-1) % mod

diceCnt = int(input())
total = 0

for _ in range(diceCnt):
    N, S = map(int, input().split())
    gcd_ns = math.gcd(N, S)
    N //= gcd_ns
    S //= gcd_ns

    total +=  S * f(N, mod-2) % mod
    total %= mod

print(total)