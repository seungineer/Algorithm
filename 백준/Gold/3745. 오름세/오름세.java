import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] arr, dp;

    static int lowerbound(int s, int e, int target) {
        while (s < e) {
            int mid = (s+e)/2;
            if(dp[mid] >= target) {
                e = mid;
            } else {
                s = mid + 1;
            }
        }
        return e;
    }
    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            String line = null;
            while ((line = br.readLine()) != null) {
                int n = Integer.parseInt(line.trim());
                arr = new int[n];
                dp = new int[n+1];

                st = new StringTokenizer(br.readLine());
                for (int i=0; i < n; i++) {
                    arr[i] = Integer.parseInt(st.nextToken());
                }

                int len = 0;
                int idx = 0;
                for (int i = 0; i<n; i++) {
                    if (arr[i] > dp[len]) {
                        dp[++len] = arr[i];
                    }
                    else {
                        idx = lowerbound(0, len, arr[i]);
                        dp[idx] = arr[i];
                    }
                }
                sb.append(len+"\n");
            }
        } catch(Exception e) {
        } finally {
            System.out.println(sb.toString());
        }


    }
}
