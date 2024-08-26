res = []
def dfs(length):
    if length == 6:
        print(*res)
        return
    for p in party:
        if res:
            if p > res[-1]:
                res.append(p)
                dfs(length+1)
                res.pop()
        else:
            res.append(p)
            dfs(length+1)
            res.pop()
    

while True:
    input_str = input().split()
    if input_str[0] == '0':
        break
    k = int(input_str[0])
    party = list(map(int, input_str[1:]))
    dfs(0)
    print()