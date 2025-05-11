import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static int cnt = 0;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        f(N, 1, 3, 2);
        System.out.println(cnt);
        System.out.println(sb);
    }

    static void f(int n, int from, int to, int other) {
        if (n==0) return;
        cnt++;
        f(n-1, from, other, to);
        sb.append(from + " " + to + "\n");
        f(n-1, other, to, from);
    }
}
