function solution(arr) {
    var answer = 0;
    arr.sort((a,b) => b -a)
    max_val = arr[0]
    isFind = false
    let res = 0
    while (!isFind) {
        res += max_val
     for (let i = 1; i< (arr.length-1); i++) {
        if (res%arr[i] == 0){
            isFind = true
        }
        else {
            isFind = false
            break
        }
    }
       
    }
    answer = res
    return answer;
}