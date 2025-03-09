import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int count = 0;
        for (int i = A; i <= B; i++) {
            if (underprime(i)) {
                count++;
            }
        }
        System.out.println(count);
    }

    private static boolean underprime(int n) {
        int count = 0;

        for (int i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                count++;
                n /= i;
            }
        }
        if (n > 1) {
            count++;
        }

        for (int i = 2; i * i <= count; i++) {
            if (count % i == 0) {
                return false;
            }
        }
        return count > 1;
    }
}