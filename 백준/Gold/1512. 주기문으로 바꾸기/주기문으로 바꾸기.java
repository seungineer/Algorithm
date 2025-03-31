import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int M;
    static char[] DNA;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        M = Integer.parseInt(br.readLine());
        DNA = br.readLine().toCharArray();
        int ans = Integer.MAX_VALUE;
        for (int p=1; p<=M; p++) {
            int pMin = 0;
            for (int idx=0; idx<p; idx++) {
                int[] atgcCnt = new int[4];
                int currentIdx = idx;
                int changeCnt = 0;
                while (currentIdx < DNA.length) {
                    if (DNA[currentIdx] == 'A') atgcCnt[0]++;
                    if (DNA[currentIdx] == 'T') atgcCnt[1]++;
                    if (DNA[currentIdx] == 'G') atgcCnt[2]++;
                    if (DNA[currentIdx] == 'C') atgcCnt[3]++;
                    currentIdx += p;
                }
                int maxCnt = -1;
                for (int cnt: atgcCnt) {
                    maxCnt = Math.max(maxCnt, cnt);
                    changeCnt += cnt;
                }
                changeCnt -= maxCnt;
                pMin += changeCnt;
            }
            ans = Math.min(ans, pMin);
        }
        System.out.println(ans);
    }
}
