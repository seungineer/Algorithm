import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        char[] sArr = s.toCharArray();
        boolean isFirst = true;
        for (char c: sArr) {
            if (c == ' ') {
                sb.append(c);
                isFirst = true;
                continue;
            }
            if (isFirst) {
                sb.append(Character.toUpperCase(c));
                isFirst = false;
                continue;
            }
            sb.append(Character.toLowerCase(c));
        }
        
        return sb.toString();
    }
}