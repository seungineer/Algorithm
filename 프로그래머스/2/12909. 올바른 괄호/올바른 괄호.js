function solution(s){
    var answer = true;
    let stk = [];
    for (k of s){
        if (k === '('){
            stk.push(k)
        }
        else {
            if (stk.length === 0) {
                return false
            }
            stk.pop()
        }
    }
    if (stk.length == 0){
        return true
    }
    else {
        return false
    }
}