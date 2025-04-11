import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {
    static char[][] matrix = new char[5][5];
    static int[] comb = new int[7];
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int cnt = 0;
    static int connCnt = 0;

    static int bfs(int stX, int stY, int[][] newMatrix) {
        int connected = 0;
        Queue<int[]> qu = new ArrayDeque<>();
        qu.offer(new int[] {stX, stY});
        newMatrix[stX][stY] = 0;
        while (!qu.isEmpty()) {
            int[] newPoint = qu.poll();
            int x = newPoint[0];
            int y = newPoint[1];
            connected++;
            for (int k=0; k<4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <=nx && nx < 5 && 0 <= ny && ny < 5) {
                    if (newMatrix[nx][ny] == 1) {
                        newMatrix[nx][ny] = 0;
                        qu.offer(new int[] {nx, ny});
                    }
                }
            }
        }
        return connected;
    }

    static boolean isAllConnected() {
        int[][] newMatrix = new int[5][5];
        for (int n: comb) {
            int x = n / 5;
            int y = n % 5;
            newMatrix[x][y] = 1;
        }
        outter: for (int i=0; i<5; i++) {
            for (int j=0; j<5; j++) {
                if (newMatrix[i][j] == 1) {
                    connCnt = bfs(i, j, newMatrix);
                    break outter;
                }
            }
        }
        if (connCnt == 7) return true;
        return false;
    }

    static boolean isDasom() {
        int cntS = 0;
        int cntY = 0;
        int[][] newMatrix = new int[5][5];
        for (int n: comb) {
            int x = n / 5;
            int y = n % 5;
            if (matrix[x][y] == 'S') {
                cntS++;
            } else {
                cntY++;
            }
        }
        return  cntS > cntY;
    }

    static void bt(int number, int idx) {
        if (idx != -1) {
            if (idx > 6) return;
            comb[idx] = number;
            if (idx == 6) {
                if (isDasom() && isAllConnected()) {
                    cnt++;
                }
                return;
            }
        }

        for (int next=number+1; next<25; next++) {
            bt(next, idx+1);
        }
    }

    public static void main(String[] args) throws IOException {
//        모든 가능합 조합에 대해 백트래킹 진행
//        7개의 조합이 완성된 경우 모두 커넥션되어 있는지 확인
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        matrix = new char[5][5];
        for (int i=0; i<5; i++) {
            matrix[i] = br.readLine().toCharArray();
        }

        bt(-1, -1);
        System.out.println(cnt);

    }
}
