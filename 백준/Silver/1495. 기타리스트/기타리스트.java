import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        boolean[][] dp = new boolean[N+1][M+1];
        String[] vol = br.readLine().split(" ");
        int[] volumes = new int[N];

        for (int i=0; i<N; i++) {
            int v = Integer.parseInt(vol[i]);
            volumes[i] = v;
        }
        dp[0][S] = true;
        for (int i=1; i<N+1; i++) {
            for (int j=0; j<M+1; j++) {
                if (!dp[i-1][j]) continue;
                if (j - volumes[i-1] >= 0) {
                    dp[i][j-volumes[i-1]] = true;
                }
                if (j + volumes[i-1] <= M) {
                    dp[i][j+volumes[i-1]] = true;
                }
            }
        }
        int ans = -1;
        for (int i=0; i<M+1; i++) {
            if (dp[N][i]) {
                ans = i;
            }
        }
        System.out.println(ans);
    }
}