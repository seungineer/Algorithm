a, b = map(int, input().split())

m = int(b**0.5)
isPrime = [True for _ in range(b+1)]
isPrime[1] = False
for i in range(2, m+1):
    j = i**2
    for k in range(j, b+1, i):
        isPrime[k] = False
for l in range(a, b+1):
    if isPrime[l] == True:
        print(l)