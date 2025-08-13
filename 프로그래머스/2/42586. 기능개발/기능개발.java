import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // System.out.println(Arrays.toString(progresses));
        for (int i=0; i<progresses.length; i++) {
            progresses[i] = (100 - progresses[i]) / speeds[i];
            if ((100 - progresses[i]) % speeds[i] != 0) {
                progresses[i]++;
            }
        }
        Queue<Integer> stk = new LinkedList<>();
        // System.out.println(Arrays.toString(progresses));
        ArrayList<Integer> ans = new ArrayList<>();
        
        int cnt = 0;
        for (int num: progresses) {
            if (stk.size() == 0) {
                stk.add(num);
                cnt++;
                continue;
            }
            if (stk.peek() >= num) {
                cnt++;
            } else {
                stk.poll();
                stk.add(num);
                ans.add(cnt);
                cnt = 1;
            }
            
        }
        if (stk.size() != 0) {
            ans.add(cnt);
        }
        int[] answer = new int[ans.size()];
        for (int i=0; i<ans.size(); i++) {
            answer[i] = ans.get(i);
        }
        return answer;
    }
}