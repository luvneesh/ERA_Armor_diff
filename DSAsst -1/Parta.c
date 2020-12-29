#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
long long int counter(long long  n,long long int m){
    if(m==1){
        return 0;
    }
    else if(m==2)
        return n-1;
    else if (m==0)
        return 1;
    else {
        return ((n-1) * counter(n,m-2) + (n-2)*counter(n,m-1)%1000000007);
    }
}
// int counter (int n, int m){
//     if (m==1)
//         return 1;
//     else if (m==0)
//         return 0;
//     else 
//         return  n-1*counter(n,m-1);
// }
// int counter(int n,int m){
//     int ret=1;
//     int sum=0;
//     ret=n-2;
//     // return ret;
//     for( double int i=1;i<=m-2;i++){
//         sum+=(pow(n-1,i)%1000000007);
//     }
//     ret*=sum;
//     return ret;
//     }

int main() {
    
    long long int n,m;
    scanf("%lld %lld",&n,&m);
    // if (m>2){
        
    
    long long count=counter(n,m)%1000000007;
    printf("%lld",count);
    
    // }
    // else 
    //     printf("0");
}
