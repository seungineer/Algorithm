class Solution {
    public int solution(int n) {
        int answer = n;
        int bitCntN = Integer.bitCount(n);
        // 1의 개수가 같으면서 더 큰 수
        answer++;
        while (true) {
            if (Integer.bitCount(answer) == bitCntN) {
                return answer;
            }
            answer++;
        }
    }
}