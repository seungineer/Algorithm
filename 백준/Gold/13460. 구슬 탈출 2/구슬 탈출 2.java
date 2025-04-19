import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
//        기울이는 동작의 백트래킹(이전 움직임은 다음 움직임에서 배제)
//        기울이는 방향을 기준으로 벽에서 더 가까운 블럭 먼저 이동
//        중력의 이동은 while 문을 이용
//          이동 중 구멍을 만나는 경우 check
//              두 블럭이 모두 구멍에 들어가는 경우 배제
//
//        기존 매트릭스에서 newPoint 위치를 만들면,
//          기존 매트릭스 수정
//        백트래킹 복귀 시 원상복귀

//        방향이 0, 1, 2, 3이라고 하면,
//        while 문 안에서 해당 인덱스로 dx, dy 진행
    static int N;
    static int M;
    static char[][] matrix;
    static int[] pointR = new int[2];
    static int[] pointB = new int[2];
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static boolean isDroppedR;
    static boolean isDroppedB;
    static int ans = 11;

    public static void restoreMatrix() {
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (matrix[i][j] == 'R') matrix[i][j] = '.';
                if (matrix[i][j] == 'B') matrix[i][j] = '.';
            }
        }
    }

    public static void moveBlueRed(int currDir) {
        // blue 이동
        matrix[pointB[0]][pointB[1]] = '.';
        while (true) {
            int x = pointB[0];
            int y = pointB[1];
            int nx = x + dx[currDir];
            int ny = y + dy[currDir];
            if (matrix[nx][ny] == '.') {
                pointB[0] = nx;
                pointB[1] = ny;
            }
            if (matrix[nx][ny] == 'O') {
                isDroppedB = true;
                break;
            }
            if (matrix[nx][ny] == '#' || matrix[nx][ny] == 'R') break;
        }
        if (!isDroppedB) matrix[pointB[0]][pointB[1]] = 'B';
        // red 이동
        matrix[pointR[0]][pointR[1]] = '.';
        while (true) {
            int x = pointR[0];
            int y = pointR[1];
            int nx = x + dx[currDir];
            int ny = y + dy[currDir];
            if (matrix[nx][ny] == '.') {
                pointR[0] = nx;
                pointR[1] = ny;
            }
            if (matrix[nx][ny] == 'O') {
                isDroppedR = true;
                break;
            }
            if (matrix[nx][ny] == '#' || matrix[nx][ny] == 'B') break;
        }
        if (!isDroppedR) matrix[pointR[0]][pointR[1]] = 'R';
    }

    public static void moveRedBlue(int currDir) {
        // red 이동
        matrix[pointR[0]][pointR[1]] = '.';
        while (true) {
            int x = pointR[0];
            int y = pointR[1];
            int nx = x + dx[currDir];
            int ny = y + dy[currDir];
            if (matrix[nx][ny] == '.') {
                pointR[0] = nx;
                pointR[1] = ny;
            }
            if (matrix[nx][ny] == 'O') {
                isDroppedR = true;
                break;
            }
            if (matrix[nx][ny] == '#' || matrix[nx][ny] == 'B') break;
        }
        if (!isDroppedR) matrix[pointR[0]][pointR[1]] = 'R';

        // blue 이동
        matrix[pointB[0]][pointB[1]] = '.';
        while (true) {
            int x = pointB[0];
            int y = pointB[1];
            int nx = x + dx[currDir];
            int ny = y + dy[currDir];
            if (matrix[nx][ny] == '.') {
                pointB[0] = nx;
                pointB[1] = ny;
            }
            if (matrix[nx][ny] == 'O') {
                isDroppedB = true;
                break;
            }
            if (matrix[nx][ny] == '#' || matrix[nx][ny] == 'R') break;
        }
        if (!isDroppedB) matrix[pointB[0]][pointB[1]] = 'B';
    }

    public static void bt(int currDir, int currIterCnt) {
        if (currIterCnt >= ans) return;
        if (currIterCnt == 11) return;
        // currdir 방향으로 움직여서 포인트 알, 비 수정하기
        isDroppedR = false;
        isDroppedB = false;
        if (pointR[0] <= pointB[0]) {
            if (currDir == 0) {
                // 블루 먼저 움직이기
                moveBlueRed(currDir);
            }
            if (currDir == 1) {
                // 레드 먼저 움직이기
                moveRedBlue(currDir);
            }
        } else {
            if (currDir == 0) {
                // 레드 먼저 움직이기
                moveRedBlue(currDir);
            }
            if (currDir == 1) {
                // 블루 먼저 움직이기
                moveBlueRed(currDir);
            }
        }
        if (pointR[1] <= pointB[1]) {
            if (currDir == 2) {
                // 블루 먼저 움직이기
                moveBlueRed(currDir);
            }
            if (currDir == 3) {
                // 레드 먼저 움직이기
                moveRedBlue(currDir);
            }
        } else {
            if (currDir == 2) {
                // 레드 먼저 움직이기
                moveRedBlue(currDir);
            }
            if (currDir == 3) {
                // 블루 먼저 움직이기
                moveBlueRed(currDir);
            }
        }
        if (!isDroppedB && isDroppedR) {
            ans = Math.min(ans, currIterCnt);
            return;
        }
        if (isDroppedB || isDroppedR) return;

        for (int dir=0; dir<4; dir++) {
            if (dir == currDir) continue;
            int pBx = pointB[0];
            int pBy = pointB[1];
            int pRx = pointR[0];
            int pRy = pointR[1];
            bt(dir, currIterCnt+1);
            restoreMatrix();
            matrix[pBx][pBy] = 'B';
            matrix[pRx][pRy] = 'R';

            pointB[0] = pBx;
            pointB[1] = pBy;
            pointR[0] = pRx;
            pointR[1] = pRy;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        matrix = new char[N][M];
        for (int i=0; i<N; i++) {
            matrix[i] = br.readLine().toCharArray();
        }
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (matrix[i][j] == 'B') {
                    pointB[0] = i;
                    pointB[1] = j;
                }
                if (matrix[i][j] == 'R') {
                    pointR[0] = i;
                    pointR[1] = j;
                }
            }
        }

        for (int dir=0; dir<4; dir++) {
            int iterCnt = 1;
            int pBx = pointB[0];
            int pBy = pointB[1];
            int pRx = pointR[0];
            int pRy = pointR[1];
            bt(dir, iterCnt);
            restoreMatrix();
            matrix[pBx][pBy] = 'B';
            matrix[pRx][pRy] = 'R';

            pointB[0] = pBx;
            pointB[1] = pBy;
            pointR[0] = pRx;
            pointR[1] = pRy;
        }
        if (ans == 11) ans = -1;
        System.out.println(ans);
    }
}
