n = int(input())
#로직

route = []
cnt =[0]

def hanoi(start, end, n):
    
    if n ==1:
        route.append([start,end])
        cnt[0] += 1
        return

    aux = 6 - start - end
    
    hanoi(start, aux, n-1) # n-1개를 보조에 우선 이동
    route.append([start, end])
    cnt[0] += 1
    hanoi(aux, end, n-1)

if n <= 20:
    hanoi(1, 3, n)
    print(cnt[0])
    for e in route:
        print(f"{e[0]} {e[1]}")
else:
    print(2**n - 1)