lst = list(map(int, input().split()))
for i in range(len(lst)): lst[i] *= lst[i]
print((sum(lst)%10))