t = int(input())
fibo = [0 for _ in range(41)]
fibo[0] = 1
fibo[1] = 1

for i in range(2, 40+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
    
for _ in range(t):
    n = int(input())
    if n == 0 :
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibo[n-2], fibo[n-1])