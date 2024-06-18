function solution(n) {
    let cnt = 1
    let num = 2
    let a = 0
    while (1) {
        a = (num-1)*(num)/2
        if (a>=n){
            break
        }
        if (Math.floor((n - a)%num) === 0){
            cnt += 1
        }
        num += 1
    }
    console.log(cnt)
    return cnt
}