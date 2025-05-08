import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static long[] cntElements;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int cntDigit = String.valueOf(N).length();
        cntElements = new long[cntDigit + 2]; // index 0은 사용 안함

        // 자리수별 전체 자릿수 개수 계산 (1자리 ~ cntDigit자리)
        long base = 1;
        for (int i = 1; i <= cntDigit; i++) {
            cntElements[i] = i * 9L * base;
            base *= 10;
        }

        // 현재 숫자까지의 총 자릿수 합계
        long sum = 0;
        int targetIdx = -1;

        for (int i = 1; i <= cntDigit; i++) {
            sum += cntElements[i];
            if (sum >= K) {
                targetIdx = i;
                break;
            }
        }

        if (targetIdx == -1) {
            System.out.println(-1);
            return;
        }

        // 자릿수가 targetIdx인 숫자에서 몇 번째 자리인지
        long prevSum = sum - cntElements[targetIdx];
        long X = K - prevSum;

        long BASE = (long) Math.pow(10, targetIdx - 1);
        long targetNum = BASE + (X - 1) / targetIdx;

        if (targetNum > N) {
            System.out.println(-1);
            return;
        }

        String targetStr = String.valueOf(targetNum);
        int charIdx = (int) ((X - 1) % targetIdx);
        System.out.println(targetStr.charAt(charIdx));
    }
}
