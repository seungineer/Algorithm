N = int(input())
seq = list(map(int, input().split()))


arr = [[seq[i]] for i in range(N)]
answer = [seq[0]]

for en in range(1, N):
    for i in range(en):
        if seq[en] > seq[i]:
            if len(arr[en]) < len(arr[i]) + 1:
                arr[en] = [k for k in arr[i]]
                arr[en].append(seq[en])
                if len(answer) < len(arr[en]):
                    answer = [k for k in arr[en]]

print(len(answer))
print(*answer)
