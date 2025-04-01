import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int T;
    public static void main(String[] args) throws IOException {
        long[][] dp = new long[65][10];
        for (int i=0; i<10; i++)  dp[1][i] = 1;
        for (int i=2; i<65; i++) {
            for (int j=0; j<10; j++) {
                for (int k=j; k<10; k++) {
                    dp[i][k] += dp[i-1][j];
                }
            }
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int temp=0; temp<T; temp++) {
            int n = Integer.parseInt(br.readLine());
            System.out.println(Arrays.stream(dp[n]).sum());
        }
    }
}
