class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        graph = {}
        for k in edges:
            if k[0] in graph.keys():
                graph[k[0]].append(k[1])
            else:
                graph[k[0]] = [k[1]] #하위 노드만 포함
            if k[1] in graph.keys():
                graph[k[1]].append(k[0])
            else:
                graph[k[1]] = [k[0]] #하위 노드만 포함
        res = [0]
        def dfs(node, parent):
            if not node in graph.keys():
                return 1
            sets = set()
            tot = 1
            for k in graph[node]:
                if k == parent:
                    continue
                temp = dfs(k, node)
                sets.add(temp)
                tot += temp

            if len(sets) <= 1:
                res[0] += 1

            return tot
        dfs(0,-1)

        return(res[0])  