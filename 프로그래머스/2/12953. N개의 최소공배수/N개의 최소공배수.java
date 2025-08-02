import java.util.*;

class Solution {
    static int answer = 1;
    public int solution(int[] arr) {
        // 소인수분해를 해서
        // 각 수가 갖는 소인수의 개수 중 최댓값 구하기
        boolean[] isPrime = new boolean[101];
        for (int i=2; i<101; i++) isPrime[i] = true;
        
        for (int i=2; i<101; i++) {
            if (!isPrime[i]) continue;
            for (int j=2; j<101; j++) {
                int idx = i * j;
                if (idx > 101) break;
                isPrime[idx] = false;
            }
        }
        HashMap<Integer, Integer> maxCnt = new HashMap<>();
        for (int el: arr) {
            // el을 소인수 분해해서 개수 세기
            for (int i=2; i<101; i++) {
                if (!isPrime[i]) continue;
                int cnt = 0;
                while (el % i == 0) {
                    el /= i;
                    cnt ++;
                }
                int m = maxCnt.getOrDefault(i, 0);
                if (m < cnt) {
                    maxCnt.put(i, cnt);
                }
            }
        }
        maxCnt.forEach((key, val) -> {
            answer *= Math.pow(key, val);
        });
        return answer;
    }
}