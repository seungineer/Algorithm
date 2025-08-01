import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;
        // 2로 안 나뉘어 떨어지면 ans++;
        // -1 하고, 다시 2로 나누기
        while (n != 0) {
            if (n % 2 == 0) {
                n /= 2;
                continue;
            }
            n--;
            ans++;
        }
        

        return ans;
    }
}