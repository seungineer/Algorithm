function solution(people, limit) {
    var answer = 0;
    people.sort((a,b) => b-a)
    let st = 0
    let en = people.length - 1
    while (st <= en){
        if (st == en){
            answer ++
            break
        }
        if(people[st] + people[en] <= limit){
            en --
        }
        st ++
        answer ++
    }
    return answer;
}