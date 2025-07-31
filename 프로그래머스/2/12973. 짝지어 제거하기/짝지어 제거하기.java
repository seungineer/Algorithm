class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        StringBuilder sb = new StringBuilder();
        for (char k: s.toCharArray()) {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == k) {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(k);
            }
        }
        
        if (sb.length() == 0) {
            answer = 1;
        } else {
            answer = 0;
        }

        return answer;
    }
}