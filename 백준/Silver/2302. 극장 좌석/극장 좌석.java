import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int[] dp = new int[41];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < 41; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        int ans = 1;
        int prevIdx = 0;
        for (int i = 0; i < M; i++) {
            int vipIdx = Integer.parseInt(br.readLine());
            ans *= dp[vipIdx - 1 - prevIdx];
            prevIdx = vipIdx;
        }
        ans *= dp[N-prevIdx];
        bw.write(ans+"\n");
        bw.flush();
        bw.close();
        br.close();


    }
}