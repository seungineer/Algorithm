n = int(input())

time_table = []
for i in range(n):
    st, en = map(int, input().split())
    duration = en - st
    # 시작, 지속시간, 끝[ [1, 3, 4], [3, 2, 5], ... , [12, 2, 14] ]
    time_table.append([st, duration, en])

time_table.sort(key=lambda x :(x[2],x[0]))

cnt = 0
last_endtime = 0

# candidate_lst = []

for i in range(len(time_table)):
    # if last_endtime == time_table[i][2]:
    #     candidate_lst.append()

    if last_endtime <= time_table[i][0] or (): # 지난 회의 끝 시점 < 지금 회의 시작 시점
        last_endtime = time_table[i][2]
        cnt += 1 # 횟수 추가
print(cnt)