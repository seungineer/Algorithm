function solution(n) {
    var answer = 0;
    let dp = Array(n);
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for (let i = 3; i < n+1; i++) {
        dp[i] = (dp[i-1] + dp[i-2])%1234567 
    }
    answer = dp[n]
    
    return answer%1234567;
}