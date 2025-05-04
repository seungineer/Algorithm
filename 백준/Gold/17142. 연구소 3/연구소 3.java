import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[][] matrix;
    static int ans = Integer.MAX_VALUE;
    static int[] dx = new int[] {1, -1, 0, 0};
    static int[] dy = new int[] {0, 0, 1, -1};
    static int targetCnt = 0;
    static List<int[]> viruses = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        matrix = new int[N][N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
                if (matrix[i][j] == 0) targetCnt++;
                else if (matrix[i][j] == 2) viruses.add(new int[]{i, j});
            }
        }

        comb(0, 0, new int[M][]);
        if (ans == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }
    }

    static void comb(int start, int cnt, int[][] selected) {
        if (cnt == M) {
            bfs(selected);
            return;
        }

        for (int i = start; i < viruses.size(); i++) {
            selected[cnt] = viruses.get(i);
            comb(i + 1, cnt + 1, selected);
        }
    }

    static void bfs(int[][] activeViruses) {
        Queue<int[]> qu = new LinkedList<>();
        int[][] depth = new int[N][N];
        int[][] vis = new int[N][N];
        int maxD = 0;
        int cnt = 0;
        for (int[] d : depth) Arrays.fill(d, Integer.MAX_VALUE);

        // 활성 바이러스 초기화
        for (int[] pos : activeViruses) {
            qu.offer(new int[]{pos[0], pos[1], 0});
            vis[pos[0]][pos[1]] = 1;
            depth[pos[0]][pos[1]] = 0;
        }
        // vis 배열에 방문 체크
        while (!qu.isEmpty()) {
            int[] next = qu.poll();
            int x = next[0];
            int y = next[1];
            int d = next[2];
            if (depth[x][y] < d) continue;
            depth[x][y] = Math.min(depth[x][y], d);
            for (int k=0; k<4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                    if (matrix[nx][ny] == 0 || matrix[nx][ny] == 2) {
                        if (depth[nx][ny] > d + 1 && vis[nx][ny] == 0) {
                            depth[nx][ny] = d + 1;
                            vis[nx][ny] = 1;
                            qu.offer(new int[] {nx, ny, d+1});
                            if (matrix[nx][ny] == 0) {
                                cnt++;
                                maxD = Math.max(maxD, d+1);
                            }
                        }
                    }
                }
            }
        }
        // vis 배열 && matrix를 보면서 matrix가 0인데 vis가 1이 아닌 경우 확인
        boolean isFilled = true;
        if (cnt != targetCnt) isFilled = false;
        // 그런 경우가 없다면, 이번 bfs에서 cnt한 가장 오래걸리는 시간을 ans와 비교 업데이트
        if (isFilled) {
            ans = Math.min(ans, maxD);
        }
    }
}
