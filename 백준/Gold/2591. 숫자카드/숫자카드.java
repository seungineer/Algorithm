import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String data = br.readLine();
        char[] target = data.toCharArray();
        int[][] dp = new int[target.length][2];
        dp[0][0] = 1;
        dp[0][1] = 0;
        if (1 >= target.length) {
            System.out.println(1);
            return;
        }
        if (target[1] != '0') {
            dp[1][0] = 1;
            int temp = Integer.parseInt(String.valueOf(target[0]).concat(String.valueOf(target[1])));
            if (10<=temp && temp <= 34) {
                dp[1][1] = 1;
            }
        } else {
            dp[1][1] = 1;
        }
        for (int i=2; i<target.length; i++) {
            if (target[i] != '0') {
                dp[i][0] = dp[i-1][0] + dp[i-1][1];
                int temp = Integer.parseInt(String.valueOf(target[i-1]).concat(String.valueOf(target[i])));
                if (10<=temp && temp <=34) {
                    dp[i][1] = dp[i-2][0] + dp[i-2][1];
                }
            } else {
                dp[i][1] = dp[i-2][0] + dp[i-2][1];
            }
        }
        System.out.println(dp[target.length-1][0] + dp[target.length-1][1]);
    }
}
