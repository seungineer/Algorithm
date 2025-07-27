import java.util.*;

class Solution {
    boolean solution(String s) {
        // '('가 오면 stk 값을 하나 올리고,
        // ')'가 오면, stk 값을 하나 뺀다.
        // stk 값이 0으로 끝나면 true
        // 음수가 되거나 0이 아닌 수로 끝나면 false
        char[] sArr = s.toCharArray();
        int stk = 0;
        
        for (char k: sArr) {
            if (k == '(') {
                stk++;
                continue;
            }
            if (k ==')') {
                stk--;
                if (stk < 0) {
                    return false;
                }
            }
        }
        if (stk != 0) {
            return false;
        }
        return true;
    }
}