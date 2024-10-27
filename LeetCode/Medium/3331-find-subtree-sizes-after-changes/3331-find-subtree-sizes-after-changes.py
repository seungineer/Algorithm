class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:

        def dfs(node, start):
            next_node = parent[node]
            if next_node == -1: return
            if s[next_node] == s[start]:
                new_parent[start] = next_node
                return
            if next_node != -1:
                dfs(next_node, start)
        new_parent = [n for n in parent]
        for st in range(1, len(parent)):
            dfs(st, st)
        
        def dfs2(node):
            next_node = new_parent[node]
            if next_node == -1 : return
            answer[next_node] += 1
            dfs2(next_node)
    
        answer = [1 for _ in range(len(parent))]
        
        for st in range(len(parent)):
            dfs2(st)
        # print(answer)
        return (answer)