function solution(n) {
    var answer = 0;
    let arr = [0, 1]
    
    for (let i = 2; i < n+1; i++) {
        arr.push(arr[i-1]%1234567 + arr[i-2]%1234567)
     
    }
    answer = arr[n]%1234567

    
    return answer;
}