import java.util.*;

class Solution {
    static int len;
    static char[] nums;
    static boolean[] isChecked;
    static boolean[] isPrime;
    static int counts = 0;
    static Set<Integer> ans = new HashSet<>();
    public int solution(String numbers) {
        len = numbers.length();
        nums = numbers.toCharArray();
        isChecked = new boolean[len];
        isPrime = new boolean[(int)Math.pow(10, len)];
        for (int i=0; i<isPrime.length; i++) isPrime[i] = true;
        
        // isPrime 배열 만들어두기
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i=2; i<isPrime.length / 2; i++) {
            int target = i;
            if (!isPrime[target]) continue;
            target += i;
            while (target < isPrime.length) {
                isPrime[target] = false;
                target += i;
                
            }
        }
        // bt 
        // 만들어지는 숫자에 대해 char를 int로 바꿔서 isPrime 확인
        // 앞에서부터 판단이 안 들어간 경우 판단하는 로직
        for (int i=0; i<len; i++) {
            isChecked[i] = true;
            bt("" + nums[i]);
            isChecked[i] = false;
        }
        
        return ans.size();
    }
    
    static void bt(String numS) {
        int k = Integer.parseInt(numS);
        if (isPrime[k]) {
            ans.add(k);
        }
        
        for (int i=0; i<len; i++) {
            if (isChecked[i]) continue;
            isChecked[i] = true;
            bt(numS + nums[i]);
            isChecked[i] = false;
        }
    }
    
}