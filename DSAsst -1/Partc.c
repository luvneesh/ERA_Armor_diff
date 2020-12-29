#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


void multiplyinplace(long long int inputq[2][2],long long int inputw[2][2]) 
{ 
  long long int x =  inputq[0][0]*inputw[0][0] + inputq[0][1]*inputw[1][0]; 
  long long int y =  inputq[0][0]*inputw[0][1] + inputq[0][1]*inputw[1][1]; 
  long long int z =  inputq[1][0]*inputw[0][0] + inputq[1][1]*inputw[1][0]; 
  long long int w =  inputq[1][0]*inputw[0][1] + inputq[1][1]*inputw[1][1]; 
  x=x%1000000007;
y=y%1000000007;
    z=z%1000000007;
    w=w%1000000007;
  inputq[0][0] = x; 
  inputq[0][1] = y; 
  inputq[1][0] = z; 
  inputq[1][1] = w; 
} 
void power(long long int arr[2][2], long long int m,long long int n) 
{ 
  long long int i; 
  long long int Mat[2][2] = {{n-2,n-1},{1,0}}; 
  
  // n - 1 times multiply the matrix to {{1,0},{0,1}} 
  for (i = 2; i <= m; i++) 
      multiplyinplace(arr, Mat); 
}
long long pfib(long long int m,long long int n){
long long int arra[2][2] = {{n-2,n-1},{1,0}}; 
  if (m == 0) 
    return 0; 
  power(arra, m-1,n); 
  return arra[0][0]; }
int main() {
    long long int m;
    long long int n;
    
    scanf("%lld %lld",&n,&m);
    if(m==1){
        printf("0");
    }
    else if(m==2)
         printf("%lld",n-1);
    else if (m==0)
         printf("1");
    else {
    printf("%lld",pfib(m,n));}

        
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
