import java.util.*;

class Solution {
    static long MOD = 1234567;
    public long solution(int n) {
        if (n == 1) return 1;
        
        long[] dp = new long[n+1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i=3; i<n+1; i++) {
            dp[i] = ((dp[i-1]) % MOD + (dp[i-2]) % MOD) % MOD;
        }
        System.out.println(Arrays.toString(dp));
        return dp[n] % MOD;
    }
}