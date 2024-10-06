class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = {}
        for inv in invocations:
            if inv[0] in graph: graph[inv[0]].append(inv[1])
            else: graph[inv[0]] = [inv[1]]
        suspicious_set = set()
        vis = [0 for _ in range(n)]
        def dfs_find_suspicious(node):
            vis[node] = 1
            suspicious_set.add(node)
            if node in graph:
                for n in graph[node]:
                    if vis[n] == 0:
                        dfs_find_suspicious(n)
                        vis[n] = 1
        dfs_find_suspicious(k)
        answer = []
        isImpossible = False
        for k in range(n):
            if k in suspicious_set: continue
            if k in graph:
                for node in graph[k]:
                    if node in suspicious_set:
                        isImpossible = True
            if isImpossible: break
            answer.append(k)
        # print(isImpossible, [i for i in range(n)])
        # print(isImpossible, answer)
        if isImpossible: return [i for i in range(n)]
        else: return answer