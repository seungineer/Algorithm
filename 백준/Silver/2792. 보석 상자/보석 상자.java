import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static int MAXGET = -1;
    static int[] jewelry;
    static boolean isValid(int mid) {
        int studentCnt = 0;
        for (int j: jewelry) {
            while (j > 0) {
                j -= mid;
                studentCnt++;
            }
        }
        if (studentCnt <= N) return true;
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        jewelry = new int[M];
        for (int i=0; i<M; i++) {
            jewelry[i] = Integer.parseInt(br.readLine());
            MAXGET = Math.max(MAXGET, jewelry[i]);
        }

        int l = 1;
        int r = MAXGET;
        int ans = Integer.MAX_VALUE;

        while (l <= r) {
            int mid = (l + r) / 2;
            if (isValid(mid)) {
                ans = Math.min(ans, mid);
                r = mid - 1;
                continue;
            }
            l = mid + 1;
        }
        System.out.println(ans);
    }
}

