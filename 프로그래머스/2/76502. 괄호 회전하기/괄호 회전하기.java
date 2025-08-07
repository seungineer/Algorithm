import java.util.*;

class Solution {
    static char[] sArr;
    static Character[] startsList = {'(', '[', '{'};
    
    static boolean isRight(int stIdx) {
        Stack<Character> st = new Stack<>();
        List<Character> starts = new ArrayList<>(Arrays.asList(startsList));
        
        for (int d=0; d<sArr.length; d++) {
            char c = sArr[(stIdx+d)%sArr.length];
            if (starts.contains(c)) {
                st.push(c);
                continue;
            } 
            if (c == ')') {
                if (st.size() > 0 && st.peek() == '(') {
                    st.pop();
                    continue;
                } else {
                    return false;
                }
            }
            if (c == ']') {
                if (st.size() > 0 && st.peek() == '[') {
                    st.pop();
                    continue;
                } else {
                    return false;
                }
            }
            if (c == '}') {
                if (st.size() > 0 && st.peek() == '{') {
                    st.pop();
                    continue;
                } else {
                    return false;
                }
            }
        }
        if (st.size() == 0) return true;
        return false;
    }
    
    public int solution(String s) {
        int answer = 0;
        
        sArr = s.toCharArray();
        for (int st=0; st<sArr.length; st++) {
            if (isRight(st)) answer++;
        }
        
        return answer;
    }
}