import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int D = Integer.parseInt(st.nextToken());
        final int K = Integer.parseInt(st.nextToken());
        int[] pibo = new int[31];
        pibo[0] = 1;
        pibo[1] = 1;
        for (int i=2; i<31; i++) {
            pibo[i] = pibo[i-1] + pibo[i-2];
        }

        int alpha = pibo[D-1];
        int beta = pibo[D-2];
        for (int x=1; x<K; x++) {
            if ((K - alpha*x) % beta == 0) {
                System.out.println(x);
                System.out.println(x + (K - alpha*x) / beta);
                break;
            }
        }

    }
}
