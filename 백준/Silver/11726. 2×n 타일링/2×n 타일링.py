import math
n = int(input())

a = 0
sum = 0
while True:
    if (n - a) % 2 == 0:
        b = (n-a)//2
        sum += math.factorial(a+b)//(math.factorial(a)*math.factorial(b))%10007
    if n - a < 0:
        break
    a += 1

print(sum%10007)