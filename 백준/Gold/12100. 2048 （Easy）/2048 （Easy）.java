import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[][] matrix;
    static int[][] maniMatrix;
    static int[] directions = new int[] {0, 1, 2, 3}; // 상 우 하 좌
    static int ans = -1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        matrix = new int[N][N];
        int[][] orgMatrix = new int[N][N];
        StringTokenizer st;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int dir: directions) {
            cpyMatrix(orgMatrix);
            bt(dir, 0);
            restoreMatrix(orgMatrix);
        }
        System.out.println(ans);
    }

    public static void bt(int dir, int cnt) {
        if (cnt == 5) {
            findMaxValue();
            return;
        }
        maniMatrix = new int[N][N];
        int[][] orgMatrix = new int[N][N];
        rotateMatrix(matrix, maniMatrix, 0, dir);
        // maniMatrix를 0 방향으로 squeeze
        squeeze();
        rotateMatrix(maniMatrix, matrix, dir, 0);
        for (int nextDir: directions) {
            cpyMatrix(orgMatrix);
            bt(nextDir, cnt+1);
            restoreMatrix(orgMatrix);
        }
    }
    public static void rotateMatrix(int[][] curMatrix, int[][] targetMatrix, int targetDir, int curDir) {
        double rad = (Math.PI / 2) * (curDir - targetDir);
        float half = (float) 2;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                // 점 N/2 만큼 마이너스 이동
                double x = i - (double)((N-1)/half);
                double y = j - (double)((N-1)/half);
                // 이동된 점을 회전 시키기
                double nx = (Math.cos(rad) * x - Math.sin(rad) * y);
                double ny = (Math.sin(rad) * x + Math.cos(rad) * y);
                // 회전된 점 N/2 만큼 플러스 이동
                int ni =(int)Math.round(nx + (double)((N-1)/half));
                int nj =(int)Math.round(ny + (double)((N-1)/half));
                targetMatrix[ni][nj] = curMatrix[i][j];
            }
        }
    }
    public static void squeeze() {
        for (int j=0; j<N; j++) {
            Deque<Integer> stk = new ArrayDeque<>();
            Deque<Integer> qu = new ArrayDeque<>();
            for (int k=0; k<N; k++) {
                if (maniMatrix[k][j] == 0) continue;
                if (stk.size() == 0) {
                    stk.addLast(maniMatrix[k][j]);
                    continue;
                }
                if (stk.peekLast() == maniMatrix[k][j]) {
                    stk.addLast(stk.pollLast() * 2);
                    while (stk.size() != 0) {
                        qu.addLast(stk.pollFirst());
                    }
                    continue;
                }
                stk.addLast(maniMatrix[k][j]);
            }
            while (!stk.isEmpty()) {
                qu.addLast(stk.pollFirst());
            }
            while (qu.size() != N) {
                qu.addLast(0);
            }
            for (int k=0; k<N; k++) {
                int val = qu.pollFirst();
                maniMatrix[k][j] = val;
            }
        }
    }
    public static void cpyMatrix(int[][] orgMatrix) {
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                orgMatrix[i][j] = matrix[i][j];
            }
        }
    }
    public static void restoreMatrix(int[][] orgMatrix) {
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                matrix[i][j] = orgMatrix[i][j];
            }
        }
    }
    public static void findMaxValue() {
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                ans = Math.max(ans, matrix[i][j]);
            }
        }
    }
}