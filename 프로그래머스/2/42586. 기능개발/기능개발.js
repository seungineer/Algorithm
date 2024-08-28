function solution(progresses, speeds) {
    progresses.forEach((v, i) => {
        let leftprogress = 100 - v;
        let leftdays;
        if (leftprogress % speeds[i]) {
            leftdays = Math.floor(leftprogress/speeds[i]) + 1;
        } else {
            leftdays = Math.floor(leftprogress/speeds[i]);
        };
        progresses[i] = leftdays;
    })
    let target = -1;
    let cnt = 0;
    const answer = [];
    for (let i = 0; i < progresses.length; i ++) {
        if (target === -1) {
            target = progresses[i];
            cnt ++;
            continue
        }
        if (target >= progresses[i]) {
            cnt ++
        } else {
            target = progresses[i];
            answer.push(cnt);
            cnt = 1;
        }    
    }
    console.log(cnt)
    if (cnt != 0) {
        answer.push(cnt)
    }
    
    return answer;
}