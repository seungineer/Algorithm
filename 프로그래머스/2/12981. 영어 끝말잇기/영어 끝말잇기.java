import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {};
        String prev = words[0];
        HashSet<String> alreadyUsed = new HashSet<>();
        alreadyUsed.add(prev);
        
        for (int i=1; i<words.length; i++) {
            String curr = words[i];
            if (prev.charAt(prev.length() - 1) == curr.charAt(0) && !alreadyUsed.contains(curr)) {
                prev = curr;
                alreadyUsed.add(curr);
                continue;
            }
            return new int[] {i%n + 1, i/n + 1};
        }

        return new int[] {0, 0};
    }
}