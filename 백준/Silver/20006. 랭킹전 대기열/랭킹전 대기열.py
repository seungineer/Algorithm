p, m = map(int, input().split())
games = []
for _ in range(p):
    level, name = input().split()
    level = int(level)
    isAdded = False
    for g in games:
        # games에 입장 가능한 방이 있는지 탐색
        if len(g) == m: continue
        if abs(g[0][0] - level) <= 10:
            g.append([level, name])
            isAdded = True
            break
    if not isAdded:
        games.append([[level, name]])

for g in games:
    g.sort(key = lambda x: x[1])
    if len(g) == m:
        print("Started!")
        for el in g:
            print(el[0], el[1])
    else:
        print("Waiting!")
        for el in g:
            print(el[0], el[1])