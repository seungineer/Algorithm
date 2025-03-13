import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        long MOD = 1000000000 + 9;
        int N = 100000;
        long[][] arr = new long[N+1][3];
        arr[1][0] = 1;
        arr[2][1] = 1;
        arr[3][0] = 1;
        arr[3][1] = 1;
        arr[3][2] = 1;
        for (int i=4; i < N+1; i++) {
            arr[i][0] = (arr[i-1][1]%MOD + arr[i-1][2]%MOD) % MOD;
            arr[i][1] = (arr[i-2][0]%MOD + arr[i-2][2]%MOD) % MOD;
            arr[i][2] = (arr[i-3][0]%MOD + arr[i-3][1]%MOD) % MOD;
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int i=0; i < TC; i++) {
            int n = Integer.parseInt(br.readLine());
            System.out.println((arr[n][0]%MOD + arr[n][1]%MOD + arr[n][2]%MOD) % MOD);
        }
    }
}
