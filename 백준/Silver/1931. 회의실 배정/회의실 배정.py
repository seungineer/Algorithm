n = int(input())
timetable = []

for _ in range(n):
    st, en = map(int, input().split())
    timetable.append([st, en])

timetable.sort(key= lambda x: (x[1], x[0]))

end = timetable[0][1]
cnt = 1

for i in range(1, len(timetable)):
    if timetable[i][0] >= end:
        end = timetable[i][1]
        cnt += 1
        
print(cnt)