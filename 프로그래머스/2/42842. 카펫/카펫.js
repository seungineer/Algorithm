function solution(brown, yellow) {
    var answer = [];
    let x;
    let y;
    for (let i = 1; i < (brown+yellow); i++){
        if ((brown + 4 - 2*i) % 2 == 0) {
            console.log("here")
            y = i
            x = (brown + 4 - 2*i) / 2
            if ((x-2)*(y-2) == yellow && y <= x) {
                answer = [x, y]
                break
            }
        }
    }
    return answer;
}