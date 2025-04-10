import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] points;
    static boolean[] displayed;
    static int[] apply = {0, 1};
    static void bt(int idx, int point) {
        if (idx == N) return;
        displayed[point] = true;
        for (int a: apply) {
            if (idx + 1 >= N) continue;
            bt(idx+1, point + points[idx+1] * a);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        points = new int[N];
        displayed = new boolean[2_000_001];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int temp=0; temp<N; temp++) {
            points[temp] = Integer.parseInt(st.nextToken());
        }
        for (int a: apply) {
            bt(0, points[0] * a);
        }
        for (int i=1; i<2_000_001; i++) {
            if (displayed[i]) continue;
            System.out.println(i);
            break;
        }
    }
}
