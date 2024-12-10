N = int(input())
peoples = []
tot_people = 0
for _ in range(N):
    village, people = map(int, input().split())
    peoples.append([village, people])
    tot_people += people
peoples.sort()

acc_cnt = 0
for i in range(N):
    village, people = peoples[i]
    acc_cnt += people
    if acc_cnt >= tot_people / 2:
        print(village)
        break
