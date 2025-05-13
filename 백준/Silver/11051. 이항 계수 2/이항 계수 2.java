import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int MOD = 10007;

    // 역원 구하는 함수 (거듭제곱)
    public static long modInverse(long a, int mod) {
        long result = 1;
        long exponent = mod - 2;
        while (exponent > 0) {
            if ((exponent & 1) == 1) {
                result = (result * a) % mod;
            }
            a = (a * a) % mod;
            exponent >>= 1;
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        if (N - K < K) K = N - K;

        long kFactorial = 1L;
        long nFactorial = 1L;

        for (int temp = 1; temp <= K; temp++) {
            kFactorial = (kFactorial * temp) % MOD;
        }

        for (int temp = N - K + 1; temp <= N; temp++) {
            nFactorial = (nFactorial * temp) % MOD;
        }

        // 역원으로 나눗셈 처리
        long result = (nFactorial * modInverse(kFactorial, MOD)) % MOD;
        System.out.println(result);
    }
}
