import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N = 3;
    static int M = 3;
    static int R;
    static int C;
    static int K;
    static int ans = 0;
    static int[][] matrix = new int[100][100];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for (int i=0; i<3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<3; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (matrix[R-1][C-1] != K && ans != 101) {
           
            if (N >= M) {
                for (int i=0; i<N; i++) {
                    // 각 행에 대해서 작업
                    // j로 한 번 순회 해서 Map 만들기
                    Map<Integer, Integer> dict = new HashMap<>();
                    for (int j=0; j<M; j++) {
                        if (matrix[i][j] == 0) continue;
                        int prevCnt = dict.getOrDefault(matrix[i][j], 0);
                        dict.put(matrix[i][j], prevCnt + 1);
                    }
                    // Map -> min heap
                    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
                        if (a[0] == b[0]) return Integer.compare(a[1], b[1]); // 숫자 오름차순
                        return Integer.compare(a[0], b[0]); // 등장 횟수 오름차순
                    });

                    for (Map.Entry<Integer, Integer> entry: dict.entrySet()) {
                        int num = entry.getKey();
                        int cnt = entry.getValue();
                        pq.offer(new int[] {cnt, num});
                    }
                    // i행 matrix 업데이트
                    int idx = 0;
                    while (!pq.isEmpty() && idx != 100) {
                        int[] temp = pq.poll();
                        int cnt = temp[0];
                        int num = temp[1];              
                      
                        matrix[i][idx] = num;
                        matrix[i][++idx] = cnt;
                        idx++;
                        M = Math.max(M, idx);
                    }
                    for (int j=idx; j<100; j++) {
                        matrix[i][j] = 0;
                    }
                }
            } else {
                for (int j=0; j<M; j++) {
                    // 각 열에 대해서 작업
                    // i로 한 번 순회 해서 Map 만들기
                    Map<Integer, Integer> dict = new HashMap<>();
                    for (int i=0; i<N; i++) {
                        if (matrix[i][j] == 0) continue;
                        int prevCnt = dict.getOrDefault(matrix[i][j], 0);
                        dict.put(matrix[i][j], prevCnt + 1);
                    }

                    // Map -> min heap
                    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
                        if (a[0] == b[0]) return Integer.compare(a[1], b[1]); // 숫자 오름차순
                        return Integer.compare(a[0], b[0]); // 등장 횟수 오름차순
                    });


                    for (Map.Entry<Integer, Integer> entry: dict.entrySet()) {
                        int num = entry.getKey();
                        int cnt = entry.getValue();
                        pq.offer(new int[] {cnt, num});
                    }
                    // j열 matrix 업데이트
                    int idx = 0;
                    while (!pq.isEmpty() && idx != 100) {
                        int[] temp = pq.poll();
                        int cnt = temp[0];
                        int num = temp[1];
                        matrix[idx][j] = num;
                        matrix[++idx][j] = cnt;
                        idx++;
                        N = Math.max(N, idx);
                    }
                    for (int i=idx; i<100; i++) {
                        matrix[i][j] = 0;
                    }

                }
            }
            ans++;
        }
       
        if (ans != 101) System.out.println(ans);
        else System.out.println(-1);

    }
}