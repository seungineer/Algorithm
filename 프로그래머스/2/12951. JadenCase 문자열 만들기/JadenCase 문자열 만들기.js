function solution(s) {
    var answer = '';
    s_spt = s.split(" ")
    let res = []
    s_spt.map((v) => {
        res.push(v.charAt(0).toUpperCase()+v.slice(1).toLowerCase())
    })
    console.log(res)
    
    return(res.join(' '))  
}