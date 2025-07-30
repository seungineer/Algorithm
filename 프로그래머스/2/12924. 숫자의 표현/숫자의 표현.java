class Solution {
    public int solution(int n) {
        int answer = 0;
        int idxL = 1;
        int idxR = 1;
        int prefixSum = 1;
        while (n >= idxL) {
            if (prefixSum == n) {
                answer++;
                prefixSum -= idxL;
                idxL++;
                idxR++;
                prefixSum += idxR;
                continue;
            }
            if (prefixSum > n) {
                prefixSum -= idxL;
                idxL++;
                continue;
            }
            if (prefixSum < n) {
                if (idxR + 1 <= n) {
                    idxR++;
                    prefixSum += idxR;
                }
                continue;
            }
            
        }
        
        return answer;
    }
}