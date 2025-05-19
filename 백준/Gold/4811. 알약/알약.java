import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;
    static long[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        dp = new long[31][31];
        for (int i=0; i<31; i++) {
            for (int j=0; j<31; j++) {
                if (j > i) continue;
                else if (j==0) dp[i][j] = 1;
                else dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        while (true) {
            n = Integer.parseInt(br.readLine());
            if (n==0) break;
            System.out.println(dp[n][n]);
        }

    }
}
