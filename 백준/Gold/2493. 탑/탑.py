import sys
read = sys.stdin.readline

N = int(read())
towers = list(map(int, read().split()))
stack = []  
answer = [0] * N

for i in range(N):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0] + 1
    # 현재 탑을 스택에 추가
    stack.append((i, towers[i]))

print(*answer)