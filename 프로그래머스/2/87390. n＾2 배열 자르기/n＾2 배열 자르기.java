import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        List<Long> ans = new ArrayList<>();
        
        for (long idx = left; idx<=right; idx++) {
            long l = (idx / n) + 1;
            long m = (idx % n) + 1;
            ans.add(Math.max(l, m));
        }
        int[] answer = new int[ans.size()];
        for (int i=0; i<ans.size(); i++) {
            answer[i] = ans.get(i).intValue();
        }
        return answer;
    }
}