# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것 = 골드바흐 수
import sys

read = sys.stdin.readline
N = int(read())
data = [int(read()) for _ in range(N)]

#로직
## 주어진 수를 2로 나눠서
## 2로 나눈 두 수가 모두 소수인지 판단
def isPrime(n):
    for j in range(2, int(n**0.5) + 1):
        if n%j == 0:
            return False
    return True


for i in data:
    d1 = i//2
    d2 = i - d1

    while(True):
        if (isPrime(d1) and isPrime(d2)):
            print(f"{d1} {d2}")
            break
        else:
            d1 -= 1
            d2 += 1