import java.util.*;

class Solution {
    public String solution(String s) {
        String[] sArr = s.split(" ");
        Integer minVal = Integer.MAX_VALUE;
        Integer maxVal = Integer.MIN_VALUE;
        for (String k: sArr) {
            int val = Integer.parseInt(k);
            if (minVal > val) {
                minVal = val;
            }
            if (maxVal < val) {
                maxVal = val;
            }
        }
        String answer = minVal + " " + maxVal;
        return answer;
    }
}