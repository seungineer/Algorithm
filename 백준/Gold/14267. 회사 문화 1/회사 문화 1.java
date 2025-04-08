import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static ArrayList<Integer>[] childs;
    static int[] points;

    static void dfs(int node, int point) {
        points[node] += point;
        for (int child: childs[node]) {
            dfs(child, points[node]);
        }
    }
    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        childs = new ArrayList[N+1];
        points = new int[N+1];
        st = new StringTokenizer(br.readLine(), " ");

        for (int i=1; i<N+1; i++) {
            childs[i] = new ArrayList<Integer>();
        }

        for (int i=1; i<N+1; i++) {
            int parent = Integer.parseInt(st.nextToken());
            if (parent == -1) continue;
            childs[parent].add(i);
        }

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int node = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            points[node] += p;
        }

        dfs(1, 0);

        for (int node=1; node<N+1; node++) {
            System.out.print(points[node]);
            if (node != N) System.out.print(" ");
        }

    }
}
