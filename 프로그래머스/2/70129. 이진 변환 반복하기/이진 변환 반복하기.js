function solution(s) {
    let sum = 0
    let cnt = 0
    while (s != '1'){
        let arr_s = [...s]
        a = arr_s.length
        let filtered = arr_s.filter((value) => {return value==='1'})
        b = filtered.length
        sum += (a - b)
        cnt += 1
        s = b.toString(2)
    }
    
    return [cnt, sum];
}