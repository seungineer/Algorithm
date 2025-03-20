import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Point {
    int r, c, s;

    public Point(int r, int c, int s) {
        this.r = r;
        this.c = c;
        this.s = s;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        
        Point[] P = new Point[N];
        for(int i=0; i<N; ++i) {
            st = new StringTokenizer(br.readLine());
            P[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        int max = 0;
        for(int i=0; i<N-1; ++i) {
            for(int j=i+1; j<N; ++j) {
                if(Math.abs(P[i].r-P[j].r)<A && Math.abs(P[i].c-P[j].c)<B) {
                    int diff = Math.abs(P[i].s-P[j].s);
                    if(max<diff) max = diff;
                }
            }
        }
        System.out.print(max);
    }
}
