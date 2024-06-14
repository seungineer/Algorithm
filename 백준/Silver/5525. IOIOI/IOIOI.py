n = int(input())
m = int(input())
s = input()

window = 'I' + 'OI'*n

cnt = 0
i = 0
k = 0

while i != m:
    if s[i] == window[k]:
        k += 1
        i += 1
    else:
        i = i - k + 1
        k = 0
    
    if k == 2*n+1:
        cnt += 1
        i = i - k + 1
        k = 0

print(cnt)