function solution(elements) {
    var answer = 0;
    let res = new Set();
    const n = elements.length
    for (let i = 1; i<n+1; i++){
        for (let st = 0; st<n; st++){
            let cnt = 0
            let tot = 0
            for (let idx = st; cnt < i; idx++){
                tot += elements[idx%n]
                cnt += 1
            }
            res.add(tot)
        }
    }
    answer = res.size
    return answer;
}