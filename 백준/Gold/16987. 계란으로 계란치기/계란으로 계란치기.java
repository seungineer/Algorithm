import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] hp;
    static int[] weights;
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        hp = new int[N];
        weights = new int[N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            hp[i] = Integer.parseInt(st.nextToken());
            weights[i] = Integer.parseInt(st.nextToken());
        }
        bt(0);
        System.out.println(ans);
    }
    static void bt(int idx) {
        if (idx == N) {
            int cnt = 0;
            for (int i=0; i<N; i++) {
                if (hp[i] <= 0) cnt++;
            }
            ans = Math.max(ans, cnt);
            return;
        }
        boolean isCollision = false;
        for (int t=0; t<N; t++) {
            int[] orgHp = new int[N];
            if (idx == t || hp[idx] <= 0 || hp[t] <= 0) continue;
            isCollision = true;
            // orgHp 저장해두기
            for (int temp=0; temp<N; temp++) orgHp[temp] = hp[temp];
            // 쌍방 공격
            hp[idx] -= weights[t];
            hp[t] -= weights[idx];
            // bt 들어가기
            bt(idx + 1);
            for (int temp=0; temp<N; temp++) hp[temp] = orgHp[temp];
        }
        if (!isCollision && idx!= N) {
            bt(idx + 1);
        }
    }
}
