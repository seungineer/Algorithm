import java.util.*;

class Solution {
    static int answer = 1;
    public int solution(String[][] clothes) {
        HashMap<String, Integer> counts = new HashMap<>();
        
        for (String[] clothe: clothes) {
            String name = clothe[0];
            String clotheType = clothe[1];
            int cnt = counts.getOrDefault(clotheType, 0);
            counts.put(clotheType, cnt + 1);
        }
        counts.forEach((k, v) -> {
            answer *= (v+1);
        });
        return --answer;
    }
}