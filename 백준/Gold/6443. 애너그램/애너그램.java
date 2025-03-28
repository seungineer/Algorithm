import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static int M;
    static char[] target;
    static int[] alphabet = new int[26];

    public static void bt(String ans) {
        if (ans.length() == M) {
            System.out.println(ans);
            return;
        }
        for (int st=0; st<26; st++) {
            if (alphabet[st] > 0) {
                alphabet[st] -= 1;
                bt(ans+(char)(st+97));
                alphabet[st] += 1;
            }
        }
    }
    public static void main(String[] args) throws IOException {
//        알파벳이 몇 개 있는지?
//        시간복잡도 20^20
//        같은 알파벳 개수 = 같은 결과
//        중복 제거
//        a1 -> a2 -> b -> c
//        a2 -> a1 -> b -> c
//        뽑아쓰는 방식이면 가능
//        System.out.println((int) 'a'); -> 97
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int temp=0; temp<N; temp++) {
            target = br.readLine().toCharArray();
            M = target.length;
            for (int i=0; i<26; i++) {
                alphabet[i] = 0;
            }

            for (char el: target) {
                int elNum = (int) el;
                elNum -= 97;
                alphabet[elNum] += 1;
            }

            for (int st=0; st<26; st++) {
                if (alphabet[st] > 0) {
                    alphabet[st] -= 1;
                    String ans = "";
                    ans += (char) (st + 97);
                    bt(ans);
                    alphabet[st] += 1;
                }
            }

        }

    }

}
