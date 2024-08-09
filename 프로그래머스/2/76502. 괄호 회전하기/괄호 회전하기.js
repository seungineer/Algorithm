function solution(s) {
    var answer = 0;
    let s_lst = Array.from(s);
    let len_s = s.length;
    const map = new Map()
    map.set(')', '(')
    map.set('}', '{')
    map.set(']', '[')
    for (let start = 0; start < len_s; start++) {
        let stk = [];
        let isO = true;
        for (let i = 0; i < len_s; i++) {
            if (s[(start+i)%len_s] === '(' || s[(start+i)%len_s] === '{' || s[(start+i)%len_s] === '[') {
                stk.push(s[(start+i)%len_s])
            } else {
                const pair = map.get(s[(start+i)%len_s])
                if (pair === stk[stk.length - 1]) {
                    stk.pop()
                } else {
                    isO= false;
                    break
                }
            }
            
        } 
        if (!stk.length && isO) {
            answer ++;
        }
        
    }
    
    
    return answer;
}