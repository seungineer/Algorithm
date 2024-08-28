function solution(k, dungeons) {
    // 최대 8! time coplexity 이므로 완탐 가능
    var answer = -1;
    
    function dfs(idx, health, depth) {
        if (depth == dungeons.length) {
            return depth
        }
        if (health == 0) {
            return depth
        }
        let max_res = -1
        let isUpdate = false
        for (let i = 0; i < dungeons.length; i++ ) {
            if (vis[i] == 0) {
                if (health >= dungeons[i][0]) {
                    isUpdate = true
                    vis[i] = 1
                    let temp = dfs(i, health - dungeons[i][1], depth + 1);
                    vis[i] = 0
                    max_res = Math.max(max_res, temp)
                }
            }
        }
        if (isUpdate) {
            return max_res
        } else {
            return depth
        }    
     
    }
    
    for (let i = 0; i < dungeons.length; i++ ) {
        var vis = Array(dungeons.length).fill(0)
        vis[i] = 1;
        let res = dfs(i, k - dungeons[i][1], 1);
        answer = Math.max(res, answer)    
    }
    
    return answer;
}