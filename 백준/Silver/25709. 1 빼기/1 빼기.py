N = input()
n = N
ans = 0
while True:
    try:
        del_idx = n.index('1')
        l = len(n)
        temp1 = n[:del_idx]
        temp2 = n[del_idx+1:]
        n = str(int(temp1 + temp2))
        
    except:
        n = int(n)
        n -= 1
        n = str(n)
    ans += 1
    if n == '0':
        print(ans)
        break