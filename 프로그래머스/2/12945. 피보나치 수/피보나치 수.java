class Solution {
    static long MOD = 1234567;
    static long[] memo = new long[100001];
    
    static long fibo(int n) {
        if (memo[n] > 0) return memo[n];
        
        if (n == 0) return 0;
        if (n == 1) return 1;
        
        long res = (fibo(n-1) % MOD + fibo(n-2) % MOD) % MOD;
        memo[n] = res;
        return res;
    }
    
    public long solution(int n) {
        return fibo(n) % MOD;
    }
}