def solution(n):
    cnt = 0
    if n == 1:
        print(1)
        return
        
    for i in range(n+1, 2*n):
        if isPrime[i]: cnt += 1
    
    print(cnt)
    return
        
lists = []
while True:
    n = int(input())
    if n == 0: break
    lists.append(n)

m = max(lists)
isPrime = [1 for _ in range(2*m)]
isPrime[0] = 0
    
for i in range(2, int((2*m)**(1/2))+1):
    if isPrime[i] == 0: continue
    for j in range(2*i, 2*m, i):
        isPrime[j] = 0

for el in lists:
    solution(el)