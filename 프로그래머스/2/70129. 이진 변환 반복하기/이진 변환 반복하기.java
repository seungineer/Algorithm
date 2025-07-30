class Solution {
    public int[] solution(String s) {
        int[] answer = {};
        // 0 제거
        // 길이 체크
        // 길이를 2진수로 바꾸기
        // 반복
        int cnt0 = 0;
        int time = 0;
        while (!s.equals("1")) {
            int cnt1 = 0;
            for (char c: s.toCharArray()) {
                if (c == '1') cnt1++;
                if (c == '0') cnt0++;
            }
            time++;
            s = Integer.toBinaryString(cnt1);
        }
        answer = new int[] {time, cnt0};
        return answer;
    }
}