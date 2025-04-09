import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        long[][] arr = new long[N+1][N+1];
        for (int i=1; i < N+1; i++) {
            for (int j=1; j < N+1; j++) {
                if (i == j) continue;
                arr[i][j] = Integer.MAX_VALUE;
            }
        }
        while (true) {
            st = new StringTokenizer(br.readLine());
            int a, b;
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            if (a == -1 && b == -1) break;
            arr[a][b] = 1;
            arr[b][a] = 1;
        }
        for (int k=1; k<N+1; k++) {
            for (int i=1; i<N+1; i++) {
                for (int j=1; j<N+1; j++) {
                    if (arr[i][j] > arr[i][k] + arr[k][j]) {
                        arr[i][j] = arr[i][k] + arr[k][j];
                    }
                }
            }
        }
        int maxScore = Integer.MAX_VALUE;
        int[] scores = new int[N+1];
        for (int i=1; i<N+1; i++) {
            int score = 0;
            for (int j=1; j<N+1; j++) {
                if (arr[i][j] != Integer.MAX_VALUE) {
                    score = Math.max(score, (int)arr[i][j]);
                }
            }
            scores[i] = score;
            maxScore = Math.min(maxScore, score);
        }
        ArrayList<Integer> leader = new ArrayList<>();
        for (int number=1; number<N+1; number++) {
            if (maxScore == scores[number]) {
                leader.add(number);
            }
        }
        System.out.println(""+ maxScore + " " + leader.size());
        for (int l: leader) {
            System.out.print(l + " ");
        }
    }
}

