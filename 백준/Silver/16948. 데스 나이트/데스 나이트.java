import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[] dx = new int[] {-2, -2, 0, 0, 2, 2};
    static int[] dy = new int[] {-1, 1, -2, 2, -1, 1};
    static int[][] matrix;
    static int[][] vis;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        matrix = new int[N][N];
        vis = new int[N][N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        int r1 = Integer.parseInt(st.nextToken());
        int c1 = Integer.parseInt(st.nextToken());
        int r2 = Integer.parseInt(st.nextToken());
        int c2 = Integer.parseInt(st.nextToken());
        Deque<int[]> qu = new ArrayDeque<>();
        qu.addLast(new int[] {r1, c1, 0});
        vis[r1][c1] = 1;
        while (!qu.isEmpty()) {
            int[] point = qu.pollFirst();
            int x = point[0];
            int y = point[1];
            int cnt = point[2];
            if (x == r2 && y == c2) {
                System.out.println(cnt);
                return;
            }
            for (int k=0; k<6; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                    if (vis[nx][ny] == 1) continue;
                    vis[nx][ny] = 1;
                    qu.addLast(new int[] {nx, ny, cnt+1});
                }
            }
        }
        System.out.println(-1);
    }
}
