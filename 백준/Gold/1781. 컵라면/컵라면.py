n = int(input())
d_r = []

for _ in range(n):
    d_r.append(list(map(int, input().split())))
d_r.sort(reverse=True,key=lambda x : x[1])
d_r.sort(reverse=False,key=lambda x : x[0])
time = 0
score = []

for i in range(len(d_r)):
    if time < d_r[i][0]:
        time += 1
        score.append(d_r[i][1])
    else:
        if min(score) < d_r[i][1]:
            score.remove(min(score))
            score.append(d_r[i][1])
print(sum(score))