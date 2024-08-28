def solution(k, dungeons):

    def dfs(idx, health, depth):
        if depth == len(dungeons):
            return depth
        if health == 0:
            return depth
        res = -float("inf")
        isUpdate = False
        for i in range(len(dungeons)):
            if vis[i] == 0:
                if health >= dungeons[i][0]:
                    isUpdate = True
                    vis[i] = 1
                    temp = dfs(i, health - dungeons[i][1], depth + 1)
                    vis[i] = 0
                    res = max(temp, res)
        if not isUpdate:
            return depth
        else:
            return res
    res = -float("inf")
    for i in range(len(dungeons)):
        vis = [0 for _ in range(len(dungeons))]
        vis[i] = 1
        res = max(dfs(i, k - dungeons[i][1], 1), res)
    return res