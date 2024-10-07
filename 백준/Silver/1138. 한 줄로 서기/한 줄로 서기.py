import heapq
N = int(input())
seq = list(map(int, input().split()))
if N == 1:
    print(1)
    exit()
cand = []
for i in range(N):
    if seq[i] == 0:
        heapq.heappush(cand, i+1)
        break
answer = []
def check(ni):
    cnt = 0
    if ni in cand: return False
    if ni in answer: return False
    for ans in answer:
        if ans > ni:
            cnt += 1
    if cnt >= seq[ni - 1]: return True
    else: return False

while cand:
    answer.append(heapq.heappop(cand))
    for i in range(N):
        if check(i+1):
            heapq.heappush(cand, i+1)
print(*answer)
