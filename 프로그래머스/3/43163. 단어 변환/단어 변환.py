def solution(begin, target, words):
    answer = [1e9]
    # dfs로 탐색해가며, 알파벳이 하나 다른 것 체크
    # 쭉 가면서 target과 같은지 확인하기 이때, depth 체크
    vis = [0 for _ in range(len(words))]
    def dfs(start, depth):
        if start == target:
            answer[0] = min(answer[0], depth)
            return
        for i in range(len(words)):
            w = words[i]
            cnt = 0
            for j in range(len(w)):
                if w[j] == start[j]: cnt += 1
            if cnt == len(w) - 1 and vis[i] == 0:
                vis[i] = 1
                dfs(w, depth + 1)
                vis[i] = 0
            
    dfs(begin, 0)
    if answer[0] == 1e9:
        answer [0] = 0
    return answer[0]