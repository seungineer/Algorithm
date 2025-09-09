import java.util.*;

class Solution {
    static int receptions;
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        long answer = Long.MAX_VALUE;
        receptions = times.length;
        long l = 1;
        long r = times[times.length - 1] * (long) n;
        while (l <= r) {
            long mid = (l + r) / 2L;
            long cnt = 0L;
            for (int i=0; i<receptions; i++) {
                cnt += mid / (long)times[i];
            }
            if (cnt >= n) {
                r = mid - 1;
                answer = Math.min(answer, mid);
            } else {
                l = mid + 1;
            }
        }
        return answer;
    }
}