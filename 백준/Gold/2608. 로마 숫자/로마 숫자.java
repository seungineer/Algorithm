import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Alphabet {
        String sign;
        int number;
        Alphabet(String sign, Integer number) {
            this.sign = sign;
            this.number = number;
        }
    }

    static Integer outNumber(ArrayList<Alphabet> alphabets, char[] inputs) {
        int idx = 0;
        int cnt = 0;
        while (idx < inputs.length) {
            for (int i=0; i<alphabets.size(); i++) {
                if (alphabets.get(i).sign.length() == 1) {
                    if (alphabets.get(i).sign.equals(""+inputs[idx])) {
                        cnt += alphabets.get(i).number;
                        idx++;
                        break;
                    }
                }
                if (alphabets.get(i).sign.length() == 2) {
                    if (idx+1 >= inputs.length) continue;
                    if (alphabets.get(i).sign.equals(""+inputs[idx]+inputs[idx+1])) {
                        cnt += alphabets.get(i).number;
                        idx += 2;
                        break;
                    }
                }
            }
        }
        return cnt;

    }
    static String outRome(ArrayList<Alphabet> alphabets, Integer target) {
        int left = target;
        String ans = "";

        while (left != 0) {
            for (int i=0; i<alphabets.size(); i++) {
                if (left - alphabets.get(i).number >= 0) {
                    left -= alphabets.get(i).number;
                    ans += alphabets.get(i).sign;
                    break;
                }
            }
        }
        return ans;
    }
    public static void main(String[] args) throws IOException {
//        그리디하게 값이 큰 것부터 순서대로 맞춰가면 됨
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] inputA = br.readLine().toCharArray();
        char[] inputB = br.readLine().toCharArray();
        ArrayList<Alphabet> alphabets = new ArrayList<>();
        alphabets.add(new Alphabet("I", 1));
        alphabets.add(new Alphabet("V", 5));
        alphabets.add(new Alphabet("X", 10));
        alphabets.add(new Alphabet("L", 50));
        alphabets.add(new Alphabet("C", 100));
        alphabets.add(new Alphabet("D", 500));
        alphabets.add(new Alphabet("M", 1000));
        alphabets.add(new Alphabet("IV", 4));
        alphabets.add(new Alphabet("IX", 9));
        alphabets.add(new Alphabet("XL", 40));
        alphabets.add(new Alphabet("XC", 90));
        alphabets.add(new Alphabet("CD", 400));
        alphabets.add(new Alphabet("CM", 900));

        alphabets.sort((Comparator.comparingInt((Alphabet a) -> a.number).reversed()));
        int aNum = 0;
        int bNum = 0;
        aNum = outNumber(alphabets, inputA);
        bNum = outNumber(alphabets, inputB);
        System.out.println(aNum+bNum);
        System.out.println(outRome(alphabets, aNum+bNum));

    }
}
