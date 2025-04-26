import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static int[][] waters;
    static int[][] clouds;
    static int[][] newClouds;
    static int[][] commands;
    static int[][] directions = new int[][] {{0,-1}, {-1,-1}, {-1,0}, {-1,1}, {0,1}, {1,1}, {1,0},{1,-1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        waters = new int[N][N];
        clouds = new int[N][N];
        newClouds = new int[N][N];
        commands = new int[M][2];

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) waters[i][j] = Integer.parseInt(st.nextToken());
        }
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            commands[i][0] = Integer.parseInt(st.nextToken());
            commands[i][1] = Integer.parseInt(st.nextToken());
        }
        // 초기 구름 생성
        newClouds[N-1][0] = 1;
        newClouds[N-1][1] = 1;
        newClouds[N-2][0] = 1;
        newClouds[N-2][1] = 1;

        for (int[] command: commands) {
            // newClouds -> clouds
            for (int i=0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    clouds[i][j] = newClouds[i][j];
                    newClouds[i][j] = 0;
                }
            }
            // 구름 이동
            int dir = command[0];
            dir--;
            int dis = command[1];
            int dx = directions[dir][0];
            int dy = directions[dir][1];
            moveRainClouds(dx, dy, dis);
            // 물 복사
            copyWater();
            // newClouds
            makeNewClouds();
        }
        int ans = 0;
        for (int[] row: waters) {
            ans += Arrays.stream(row).sum();
        }
        System.out.println(ans);
    }
    public static void moveRainClouds(int dx, int dy, int dis) {
        ArrayList<int[]> nextClouds = new ArrayList<>();
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (clouds[i][j] == 1) {
                    int nx, ny;
                    clouds[i][j] = 0;
                    if (i + dx*dis >= 0) {
                        nx = (i + dx * dis) % N;
                    } else {
                        nx = N-(Math.abs(i+dx*dis) % N);
                        if (nx == N) nx = 0;
                    }
                    if (j + dy*dis >= 0) {
                        ny = (j + dy*dis) % N;
                    } else {
                        ny = N-(Math.abs(j+dy*dis) % N);
                        if (ny == N) ny = 0;
                    }
                    nextClouds.add(new int[] {nx, ny});
                }
            }
        }
        for (int[] next: nextClouds) {
            int x = next[0];
            int y = next[1];
            clouds[x][y] = 1;
            waters[x][y]++;
        }
    }
    public static void copyWater() {
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (clouds[i][j] == 1) {
                    for (int dir=1; dir<8;dir+= 2) {
                        int nx = i + directions[dir][0];
                        int ny = j + directions[dir][1];
                        if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                            if (waters[nx][ny] > 0) {
                                waters[i][j]++;
                            }
                        }
                    }
                }
            }
        }
    }
    public static void makeNewClouds() {
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (clouds[i][j] != 1 && waters[i][j] >= 2) {
                    waters[i][j] -= 2;
                    newClouds[i][j] = 1;
                    clouds[i][j] = 0;
                }
            }
        }
    }

}
