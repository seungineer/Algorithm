n = int(input())
lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))
lst_a.sort()
lst_b.sort(reverse=True)
ans = 0
for i in range(n):
    ans += lst_a[i] * lst_b[i]
print(ans)