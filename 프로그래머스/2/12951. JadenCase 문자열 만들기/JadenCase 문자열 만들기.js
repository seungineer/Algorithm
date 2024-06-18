function solution(s) {
    s_spt = s.split(" ")
    let res = []
    
    s_spt.map((v, i) => {
        temp = v[0].toUpperCase() + v.slice(1).toLowerCase()
        res.push(temp)
    })

    
    return(res.join(" "))    
}