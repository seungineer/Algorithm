import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static int R;
    static int[][] matrix;
    static int[][] newMatrix;

    public static int[] move(int x, int y, int w) {
        int nx;
        int ny;
        if (x == w) {
            if (y == w) {
                nx = x + 1;
                ny = y;
            } else {
                nx = x;
                ny = y - 1;
            }
        } else if (x == N-1-w) {
            if (y == M-1-w) {
                nx = x - 1;
                ny = y;
            } else {
                nx = x;
                ny = y + 1;
            }
        } else {
            if (y == M-1-w) {
                nx = x - 1;
                ny = y;
            } else {
                nx = x + 1;
                ny = y;
            }
        }
        return new int[] {nx, ny};
    }

    public static void main(String[] args) throws IOException {
//        껍데기(w), w or N-w에 있고 -> w or M-w에 있는 경우
//                 w or N-w에 있고 -> !w and !M-w인 경우
//        !w and !N-w에 있고 -> w인 경우
//        !w and !N-w에 있고 -> M-w인 경우
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        matrix = new int[N][M];
        for (int i=0; i<N; i++) {
            String[] row = br.readLine().split(" ");
            for (int j=0; j<M; j++) {
                matrix[i][j] = Integer.parseInt(row[j]);
            }
        }
        for (int r=0; r<R; r++) {
            newMatrix = new int[N][M];
            for (int i=0; i<N; i++) {
                for (int j=0; j<M; j++) {
                    int w = Math.min(i, N-1-i);
                    w = Math.min(w, j);
                    w = Math.min(w, M-1-j);
                    int[] newLoc = Main.move(i, j, w);
                    newMatrix[newLoc[0]][newLoc[1]] = matrix[i][j];
                }
            }
            for (int i=0; i<N; i++) {
                for (int j=0; j<M; j++) {
                    matrix[i][j] = newMatrix[i][j];
                }
            }
        }
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (j != M-1) {
                    bw.write(matrix[i][j] + " ");
                } else {
                    bw.write(""+ matrix[i][j]);
                }
            }
            if (i != N-1) bw.write("\n");
        }
        bw.flush();

    }
}
