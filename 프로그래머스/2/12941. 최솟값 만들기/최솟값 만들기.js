function solution(A,B){
    var answer = 0;
    A.sort((a, b) => a-b)
    B.sort((a, b) => b-a)
    let mul = 0;
    for (let i=0; i<A.length; i++){
        mul += A[i]*B[i]
    }
    console.log(mul)
    return mul;
}