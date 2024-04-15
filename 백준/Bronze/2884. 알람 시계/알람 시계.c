#include <stdio.h>

int main()
{
    int h, m;
    int nh, nm;
    scanf("%d %d", &h, &m);
    
    if (m < 45) {
        nh = h - 1;
        nm = 60 + (m - 45);

        if (nh < 0){
            nh = 24 + nh;
        }
    }
    else{
        nh = h;
        nm = m - 45;
    }
    printf("%d %d", nh, nm);
}