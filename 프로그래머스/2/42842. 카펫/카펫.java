class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        // 가로 * 세로 = brown + yellow
        // (가로 + 세로) * 2 - 4 = brown
        for (int m=3; m < 5001; m++) {
            int tot = brown + yellow;
            int n1 = -1;
            
            if (tot % m == 0) {
                n1 = tot / m;
            } else {
                continue;
            }
            int n2 = -1;
            if ((brown + 4) % 2 == 0) {
                n2 = ((brown + 4) / 2) - m;
            }
            if (n1 >= 3 && n2 >= 3) {
                if (n1 == n2 && m >= n1) return new int[] {m, n1};
            }
        }
        return null;
    }
}