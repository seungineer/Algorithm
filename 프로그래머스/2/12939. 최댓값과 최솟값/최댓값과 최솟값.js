function solution(s) {
    var answer = '';
    let s_lst = s.split(' ')
    let min_n = Number.MAX_SAFE_INTEGER
    let max_n = Number.MIN_SAFE_INTEGER
    for (let i = 0; i<s_lst.length; i++){
        num = s_lst[i]/1
        max_n = Math.max(num, max_n)
        min_n = Math.min(num, min_n)
    }
    let res = String(min_n) + " " + String(max_n);
    return res
}