# 1에서 100000까지 간다하면 연산횟수 100회 미만임
# 완탐기준 100회를 넘어가면 종료하는 방식으로 가능할듯
import heapq
from collections import deque
N, K = map(int, input().split())
if N > K:
    print(N-K)
    print(1)
    exit()
dp = [1e9 for _ in range(K+2)]
dp[N] = 0
answer = dict()

qu = []
heapq.heappush(qu, [0, N])
while qu:
    calCount, standard = heapq.heappop(qu)
    dp[standard] = min(dp[standard], calCount)
    if standard - 1 <= (K+1) and standard - 1 >= 0 and dp[standard-1] >= calCount + 1:
        heapq.heappush(qu, [calCount+1, standard-1])
    if standard + 1 >= 0 and standard + 1 <= (K+1) and dp[standard+1] >= calCount + 1:
        heapq.heappush(qu, [calCount+1, standard+1])
    if standard * 2 >= 0 and standard * 2 <= (K+1) and dp[standard*2] >= calCount + 1:
        heapq.heappush(qu, [calCount+1, standard*2])

targetCnt = dp[K]
answer = [0]
dp = [1e9 for _ in range(2*(K+2))]
qu = deque()
qu.append([N, 0])
while qu:
    node, count = qu.popleft()
    dp[node] = min(dp[node], count)
    if count > targetCnt: continue
    if count == targetCnt:
        if node == K: answer[0] += 1
    if node - 1 <= 2*(K+1) and node - 1 >= 0 and dp[node - 1] >= count + 1: qu.append([node - 1, count + 1])
    if node + 1 >= 0 and node + 1 <= 2*(K+1) and dp[node + 1] >= count + 1: qu.append([node + 1, count + 1])
    if node * 2 >= 0 and node * 2 <= 2*(K+1) and dp[node * 2] >= count + 1: qu.append([node * 2, count + 1])
print(targetCnt)
print(answer[0])