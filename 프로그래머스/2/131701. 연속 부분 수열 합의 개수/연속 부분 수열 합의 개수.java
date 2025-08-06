import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        HashSet<Integer> results = new HashSet<>();
        for (int k: elements) {
            results.add(k);
        }
        
        for (int l=2; l<elements.length+1; l++) {
            int initialSum = 0;
            for (int i=0; i<l; i++) {
                initialSum += elements[i];
            }
            results.add(initialSum);
            
            for (int st=1; st<elements.length; st++) {
                initialSum -= elements[st-1];
                int en = (st + l - 1) % elements.length;
                initialSum += elements[en];
                results.add(initialSum);
            }
        }
        
        answer = results.size();
        return answer;
    }
}