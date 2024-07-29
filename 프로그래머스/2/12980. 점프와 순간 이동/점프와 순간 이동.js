function solution(n)
{
    var ans = 0;
    var cnt = 0;
    while (n != 1){
        if (n%2 == 0) { //짝수이면
            n = n/2 
        }
        else {
            n--
            cnt++
        }
    }
    ans = cnt+1
    
    return ans;
}