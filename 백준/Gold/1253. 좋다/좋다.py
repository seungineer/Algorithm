# 투포인터로 풀어보기
# 최악: 2000 * 2000 = 4* 10^6

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = 0
for i in range(len(lst)):
    l = 0
    r = len(lst) - 1
    if l == i: l += 1
    if r == i: r -= 1
    while l < r:
        if lst[l] + lst[r] == lst[i]:
            if l != i and r != i:
                answer += 1
                break
            if l == i: l += 1
            if r == i: r -= 1
        elif lst[l] + lst[r] > lst[i]:
            r -= 1
        else:
            l += 1
print(answer)
