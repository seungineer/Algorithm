import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static List<Integer>[] matrix;
    static int[][] dp;
    static boolean[] vis;

    public static void dfs(int parent) {
        vis[parent] = true;
        for (int child: matrix[parent]) {
            if (vis[child]) continue;
            vis[child] = true;
            dfs(child);
            dp[parent][0] += dp[child][1];
            dp[parent][1] += Math.min(dp[child][0], dp[child][1]);
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        dp = new int[N+1][2];
        matrix = new ArrayList[N+1];
        for (int i=0; i<N+1; i++) {
            matrix[i] = new ArrayList<>();
        }
        for (int temp=0; temp<N-1; temp++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            matrix[a].add(b);
            matrix[b].add(a);
        }
        for (int node=1; node<N+1; node++) {
            dp[node][0] = 0;
            dp[node][1] = 1;
        }
        vis = new boolean[N+1];
        dfs(1);
        System.out.println(Math.min(dp[1][0], dp[1][1]));
    }
}