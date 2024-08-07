function solution(n, wires) {
    var answer = -1;
    const graph = Array.from(Array(n+1), ()=>[])
    for (const wire of wires) {
        graph[wire[0]].push(wire[1])
        graph[wire[1]].push(wire[0])
    }
    
    const bfs = (start, ban) => {
        const vis = Array.from(Array(n+1), ()=>false)
        vis[start] = true;
        let queue = [start]
        let cnt = 0;
        while (queue.length > 0) {
            cnt++
            st = queue.shift()
            for (let en of graph[st]) {
                if (vis[en] === false && en !== ban) {
                    queue.push(en)
                    vis[en] = true
                }
            }       
        }
        return cnt
    }
    min_cnt = Number.MAX_SAFE_INTEGER;
    wires.forEach((el) => {
        let cnt = bfs(el[0], el[1])
        min_cnt = Math.min(min_cnt, Math.abs(n-2*cnt))
    })
    
    return min_cnt;
}