from collections import deque
n, m = map(int, input().split())
ladder = {}
snake = {}
for _ in range(n):
    st, en = map(int, input().split())
    ladder[st] = en #{32: 62, 42: 68, 12: 98, st: en}
  
for _ in range(m):
    st, en = map(int, input().split())
    snake[st] = en #{95: 13, 97: 25, st: en}

# 1번 -> 100번 최소 횟수

# BFS로 1에서 출발해 1,                     2, 3, 4, 5, 6 거치면
#                 2,        3, 4, 5, 6, 7 거치고
#                 3, 4, 5, 6, 7,...          
# 쭉 가면

wait_st = deque()
wait_st.append([1, 0]) # [start, 주사위 굴린 횟수]
vis = [-1 for _ in range(101)] #-1이면 미방문, 1이면 방문
min_cnt = 1000
while wait_st:
    st, cnt = map(int, wait_st.popleft())
    vis[st] = 1

    for i in range(1, 7): #st에서 i 주사위가 나왔을 때
        st_1 = st + i
        # 새로운 st에 ladder, snake가 있는 경우
        if st_1 in ladder.keys():
            st_1 = ladder[st_1]
        elif st_1 in snake.keys():
            st_1 = snake[st_1]
        # 새로운 st에 아무 것도 없는 경우 그대로 st 사용
        if st_1 > 100:
            continue
        if cnt +1 > min_cnt:
            continue
        if st_1 == 100:
            min_cnt = min(min_cnt, cnt+1)
        if vis[st_1] != 1:
            wait_st.append([st_1, cnt+1])

print(min_cnt)
        