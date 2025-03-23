import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] vis;
    static char[][] matrix;
    static int[] D_X = {1, -1, 0, 0};
    static int[] D_Y = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        matrix = new char[N][M];

        for (int i=0; i<N; i++) {
            char[] charArray = br.readLine().toCharArray();
            for (int j=0; j<M; j++) {
                matrix[i][j] = charArray[j];
            }
        }

        vis = new int[N][M];
        for (int i=0; i<N; i++) {
            Arrays.fill(vis[i], 0);
        }
        int cnt_w = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (matrix[i][j] == 'W' && vis[i][j] == 0) {
                    vis[i][j] = 1;
                    int cnt = bfs(new Point(i,j), 'W');
                    cnt_w += cnt * cnt;
                }
            }
        }
        int cnt_b = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (matrix[i][j] == 'B' && vis[i][j] == 0) {
                    vis[i][j] = 1;
                    int cnt = bfs(new Point(i,j), 'B');
                    cnt_b += cnt * cnt;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(cnt_w).append(" ").append(cnt_b);
        System.out.println(sb);
    }

    public static int bfs(Point current, char target) {
        int found = 1;
        Queue<Point> qu = new ArrayDeque<>();
        qu.add(current);

        while (!qu.isEmpty()) {
            Point poll = qu.poll();
            for (int k=0; k<4; k++) {
                int nx = poll.x + D_X[k];
                int ny = poll.y + D_Y[k];
                if (0 > nx || N <= nx || 0 > ny || M <= ny) continue;
                if (matrix[nx][ny] == target && vis[nx][ny] == 0) {
                    found ++;
                    vis[nx][ny] = 1;
                    qu.add(new Point(nx, ny));
                }
            }
        }
        return found;
    }

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

}
