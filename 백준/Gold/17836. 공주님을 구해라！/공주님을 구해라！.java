import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M, T;
    static int[][] matrix;
    static int gramX, gramY;
    static int[][] vis;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        matrix = new int[N][M];
        vis = new int[N][M];

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<M; j++) {
                vis[i][j] = N * M * 2;
                matrix[i][j] = Integer.parseInt(st.nextToken());
                if (matrix[i][j] == 2) {
                    gramX = i;
                    gramY = j;
                }
            }
        }
        // gram -> N-1, M-1 거리 구하기

        // 0,0 -> N-1, M-1 거리 구하기
        Queue<int[]> qu = new ArrayDeque<>();
        qu.add(new int[] {0,0,0}); // x, y, time
        int[] dx = new int[] {1, -1, 0, 0};
        int[] dy = new int[] {0, 0, 1, -1};

        while (!qu.isEmpty()) {
            int[] temp = qu.poll();
            int x = temp[0];
            int y = temp[1];
            int time = temp[2];
            if (time > T) continue;
            for (int k=0; k<4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                    if (vis[nx][ny] > time + 1 && matrix[nx][ny] != 1) {
                        vis[nx][ny] = time + 1;
                        qu.add(new int[] {nx, ny, time+1});
                    }
                }
            }
        }
        int t1 = vis[gramX][gramY] + Math.abs(N-1 - gramX) + Math.abs(M-1 - gramY);
        int t2 = vis[N-1][M-1];
        if (Math.min(t1, t2) > T || Math.min(t1, t2) == N * M * 2) {
            System.out.println("Fail");
        } else {
            System.out.println(Math.min(t1, t2));
        }

    }
}
