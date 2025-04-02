import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String pattern = "(100+1+|01)+";

        System.out.println(br.readLine().matches(pattern) ? "SUBMARINE" : "NOISE");

    }
}
