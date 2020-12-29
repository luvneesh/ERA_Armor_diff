#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
// long long int counter(long int n,long int m)
// {
//     long long int sum=0;
//     if (m>=3)
//     {
//         for (int i=0;i<m-3;i++){
//             sum+=n-1;
//         }
//     sum+=n-2+n-2+n-1; 
//     return sum;
//     // sum+=1;
//     }   
    
//     else if (m==2)
//         return n-1;
//     else if (m==0)
//         return 1;
//     else
//         return 0;
    
// }
// long long int counter(long long int n,long long int m){
//     long long int sum =0
//     if (m==0)
//         return 1;
//     else if (m==1)
//         return 0;
//     else {
//         for (int i=0;i<m;i++)
            
//     }}
long long int counter(long long  n,long long int m){
    
    if(m==1){
        return 0;
    }
    else if(m==2)
        return n-1;
    else if (m==0)
        return 1;
    else {
        long long int prev=1;
        long long int now=0;
        long long int future;
        for (int i=2;i<=m;i++){
            future= (n-1)*prev;
            future+=(n-2)*now;
            future=future%1000000007;
            prev=now;
            now=future;
        }
        return now;
    }
}
int main() {

    long long int n,m;
    scanf("%lld %lld",&n,&m);
    long long int count=counter(n,m)%1000000007;
    printf("%lld",count);
} 