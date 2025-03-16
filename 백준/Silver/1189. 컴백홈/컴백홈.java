import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int R;
    private static int C;
    private static int K;
    private static int[] resultCnt;
    private static boolean[][] visited;

    private static boolean[][] canNotGo;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        R = Integer.parseInt(temp[0]);
        C = Integer.parseInt(temp[1]);
        K = Integer.parseInt(temp[2]);
        resultCnt = new int[R*C+1];
        visited = new boolean[R][C];
        canNotGo = new boolean[R][C];
        for (int i = 0 ; i < R ; i++) {
            temp = br.readLine().split("");
            for (int j = 0; j < C; j++) {
                if (temp[j].equals("T")) canNotGo[i][j] = true;
            }
        }
        visited[R-1][0] = true;
        dfs(0, R-1, 0);
        System.out.println(resultCnt[K]);
    }
    private static void dfs(int x, int y, int cnt) {
        cnt++;
        if (x == C-1 && y == 0) {
            resultCnt[cnt]++;
            return;
        }
        int[] moveX = {+1, -1, 0, 0};
        int[] moveY = {0, 0, +1, -1};
        for (int i = 0 ; i < 4 ; i++) {
            int toX = x + moveX[i];
            int toY = y + moveY[i];
            if (toX < 0 || toY < 0 || toX >= C || toY >= R) continue;
            if (!visited[toY][toX] && !canNotGo[toY][toX]) {
                visited[toY][toX] = true;
                dfs(toX, toY, cnt);
                visited[toY][toX] = false;
            }
        }
    }
}