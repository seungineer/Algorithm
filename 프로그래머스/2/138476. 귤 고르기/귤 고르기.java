import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> tangCnt = new HashMap<Integer, Integer>();
        
        for (int size: tangerine) {
            int cnt = tangCnt.getOrDefault(size, 0);
            tangCnt.put(size, cnt + 1);
        }
        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(tangCnt.entrySet());
        entries.sort((e1, e2) -> Integer.compare(e2.getValue(), e1.getValue()));
        
        for (Map.Entry<Integer, Integer> entry: entries) {
            if (k <= 0) break;
            k -= entry.getValue();
            answer++;
        }
        
        return answer;
    }
}