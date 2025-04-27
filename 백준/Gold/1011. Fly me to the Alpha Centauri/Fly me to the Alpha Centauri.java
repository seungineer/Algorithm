import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int TC = Integer.parseInt(br.readLine());
        for (int temp=0; temp<TC; temp++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int d = end - start;
            int sqroot = (int) Math.sqrt(d);

            if (sqroot*sqroot == d) {
                System.out.println(2*sqroot-1);
            } else if (sqroot*sqroot+sqroot >= d) {
                System.out.println(2*sqroot);
            } else {
                System.out.println(2*sqroot+1);
            }
        }

    }
}
