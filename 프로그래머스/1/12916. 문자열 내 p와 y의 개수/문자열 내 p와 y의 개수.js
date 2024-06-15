function solution(s){
    var answer = true;
    n = s.length
    let p_cnt = 0
    let y_cnt = 0
    for (let i = 0; i < n; i++){
        if (s[i] == 'p' || s[i] == 'P'){
            p_cnt++
            continue
        }
        if (s[i] == 'y' || s[i] == 'Y'){
            y_cnt++
        }
    }
    
    if (p_cnt == y_cnt){
        answer = true
    }
    else {
        answer = false
    }
    
    return answer;
}