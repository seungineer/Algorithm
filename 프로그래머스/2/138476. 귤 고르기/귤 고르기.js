function solution(k, tangerine) {
    var answer = 0;
    const dict = {};
    tangerine.forEach((x)=>(dict[x] = (dict[x] || 0) + 1))
    const arr = Object.values(dict).sort((a,b)=>b-a)
    let sub = 0
    for (let el of arr){
        sub += el
        if (sub < k){
            answer += 1
        }
        else if (sub == k){
            answer += 1
            break
        }
        else {
            answer += 1
            break
        }
    }    
    return answer;
}