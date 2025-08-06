import java.util.*;

class Solution {
    static boolean isAllValueZero (String[] want, HashMap<String, Integer> wants) {
        for (String name: want) {
            int val = wants.get(name);
            if (val > 0) return false;
        }
        return true;
    }
    
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        HashMap<String, Integer> wants = new HashMap<>();
        for (int i=0; i<want.length; i++) {
            String name = want[i];
            Integer cnt = number[i];
            wants.put(name, cnt);
        }
        // 초기 10일 결과 반영
        for (int idx = 0; idx<10; idx++) {
            String name = discount[idx];
            if (wants.containsKey(name)) {
                int cnt = wants.get(name);
                wants.put(name, cnt - 1);
            }
        }
        // wants가 모두 0인지?
        if (isAllValueZero(want, wants)) answer++;
        
        // 시작일을 늘리며 wants 조작
        for (int st=1; st<=discount.length - 10; st++) {
            int en = st + 10 - 1;
            String subName = discount[st-1];
            String addName = discount[en];
            if (wants.containsKey(subName)) {
                int val = wants.get(subName);
                wants.put(subName, val + 1);
            }
            if (wants.containsKey(addName)) {
                int val = wants.get(addName);
                wants.put(addName, val - 1);
            }
            
            if (isAllValueZero(want, wants)) answer++;
        }
        
        return answer;
    }
}