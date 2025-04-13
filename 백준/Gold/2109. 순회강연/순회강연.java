import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static class node implements Comparable<node> {
        int p;
        int d;
        public node(int p, int d) {
            this.p = p;
            this.d = d;
        }
        public int compareTo(node n) {
            if (p == n.p) return d - n.d;
            else return n.p - p;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        boolean[] vis = new boolean[10001];
        StringTokenizer st;
        PriorityQueue<node> qu = new PriorityQueue<>();
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            qu.add(new node(p, d));
        }
        int ans = 0;
        while (!qu.isEmpty()) {
            node currentNode = qu.poll();
            if (vis[currentNode.d]) {
                for (int j = currentNode.d; j > 0; j--) {
                    if (!vis[j]) {
                        vis[j] = true;
                        ans += currentNode.p;
                        break;
                    }
                }
            } else {
                vis[currentNode.d] = true;
                ans += currentNode.p;
            }
        }
        System.out.println(ans);

    }
}