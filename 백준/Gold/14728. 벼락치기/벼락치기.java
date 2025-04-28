import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int[] costs = new int[N+1];
        int[] rewards = new int[N+1];
        int[][] dp = new int[N+1][T+1];

        for (int i=1; i<N+1; i++) {
            st = new StringTokenizer(br.readLine());
            costs[i] = Integer.parseInt(st.nextToken());
            rewards[i] = Integer.parseInt(st.nextToken());
        }
        for (int part=1; part<N+1; part++) {
            for (int time=0; time<T+1; time++) {
                // 현재 파트의 비용이 time보다 큰 경우
                if (costs[part] > time) {
                    dp[part][time] = dp[part-1][time];
                    continue;
                }
                dp[part][time] = Math.max(dp[part-1][time], dp[part-1][time - costs[part]] + rewards[part]);
            }
        }
        System.out.println(dp[N][T]);
    }
}
