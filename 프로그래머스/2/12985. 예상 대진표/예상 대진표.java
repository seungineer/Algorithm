class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 0;
        //  1   2   3   4   5  6  7  8  
        // 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
        
        while (a != b) {
            answer++;
            if (a % 2 == 0) {
                a /= 2;
            } else {
                a = (a+1) / 2;
            }
            
            if (b % 2 == 0) {
                b /= 2;
            } else {
                b = (b+1) / 2;
            }
        }
        return answer;
    }
}