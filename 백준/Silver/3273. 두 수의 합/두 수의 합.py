n = int(input())
seq = list(map(int,input().split()))
x = int(input())
seq.sort()
st = 0
en = n - 1
ans = 0
while st < en :
    if seq[st] + seq[en] > x:
        en -= 1
    elif seq[st] + seq[en] == x:
        st += 1
        en -= 1
        ans += 1
    else:
        st += 1
print(ans)