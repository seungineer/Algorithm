function solution(s)
{
    var answer = -1;
    let stk = []
    for (let i = 0; i < s.length; i++) {
        if (stk.length > 0) {
            if (stk[stk.length-1] === s[i]){
                stk.pop()
            }
            else {
                stk.push(s[i])
            }   
        }
        else {
            stk.push(s[i])
        }
        
    }
    if (stk.length > 0) {
        answer = 0
    }
    else {
        answer = 1
    }

    return answer;
}