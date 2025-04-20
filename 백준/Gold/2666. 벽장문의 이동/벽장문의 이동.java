import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static ArrayList<int[]> candidates = new ArrayList<>();
    static int T;
    static int[][] minCnt = new int[21][21];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int l = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        for (int i=0; i<21; i++) {
            for (int j=0; j<21; j++) {
                minCnt[i][j] = Integer.MAX_VALUE;
            }
        }
        minCnt[l][r] = 0;
        T = Integer.parseInt(br.readLine());
        candidates.add(new int[]{l, r, 0});
        for (int temp=0; temp<T; temp++) {
            int target = Integer.parseInt(br.readLine());
            ArrayList<int[]> newCandidates = new ArrayList<>();
            for (int i=0; i<candidates.size(); i++) {
                int[] cand = candidates.get(i);
                int left = cand[0];
                int right = cand[1];
                int cnt = cand[2];
                if (left == target) {
                    newCandidates.add(new int[]{target, right, cnt});
                    continue;
                }
                if (right == target) {
                    newCandidates.add(new int[]{left, target, cnt});
                    continue;
                }
                if (target < left) {
                    newCandidates.add(new int[]{target, left, cnt + Math.abs(target - right)});
                } else {
                    newCandidates.add(new int[]{left, target, cnt + Math.abs(target - right)});
                }
                if (target < right) {
                    newCandidates.add(new int[]{target, right, cnt + Math.abs(target - left)});
                } else {
                    newCandidates.add(new int[]{right, target, cnt + Math.abs(target - left)});
                }
            }
            candidates.clear();
            for (int[] t: newCandidates) candidates.add(t);
        }
        int ans = Integer.MAX_VALUE;
        for (int[] t: candidates) {
            ans = Math.min(ans, t[2]);
        }
        System.out.println(ans);

    }
}
