function solution(priorities, location) {
    var answer = 0;
    
    var isFind = false;
    let loc_val = priorities[location];
    priorities.forEach((value, idx) => {
        priorities[idx] = [value, idx]
        
    })
    while (!isFind) {
        let maxPrior = -1;
        priorities.forEach((value, idx) => {
            maxPrior = Math.max(maxPrior, value[0])        
        })
        let target = priorities.shift()

        if (target[0] == maxPrior) {
            answer ++;
            if (target[1] == location) {
                isFind = true;
            }
        } else {
            priorities.push([target[0], target[1]]);
        }
    }
    return answer;
}