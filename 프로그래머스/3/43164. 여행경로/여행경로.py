def solution(tickets):
    answer = []
    vis = [0 for _ in range(len(tickets))]
    tickets.sort()
    temp = [0]
    def dfs(start, answer):
        if not 0 in vis:
            temp[0] = answer.copy()
            return

        for i in range(len(tickets)):
            if not 0 in vis: break
            if start == tickets[i][0] and vis[i] == 0:
                vis[i] = 1
                answer.append(tickets[i][1])
                # print(i, tickets[i], vis, answer)
                dfs(tickets[i][1], answer)
                answer.pop()
                vis[i] = 0
            if temp[0] != 0: return

    answer.append("ICN")
    dfs("ICN", answer)
    return temp[0]