#include<bits/stdc++.h>
using namespace std;
int fib[21];

double exf(double x1, int n){
//fast exponentiation
    if(n==0) return 1;
    double temp= exf(x1,n/2);
    temp*=temp;
    if(n&1){
        temp=x1*temp;
    }
    return temp;
}

double fn(double x){
    
    return (x*x)+ (exp(-1*x));
}

double fibonacci(double a,double b,double del,int n,int k){
    double l,u,fl,fu;
    int i=1;
    if(n==k)return b;
    while(b-a>del&&i<18){
        cout<<a<<"=a   b="<<b<<"\n";
        l= a+ (((double)fib[n-k-1]/fib[n-k+1]))*(b-a);

        u= a+ ((double)fib[n-k]/fib[n-k+1])*(b-a);
        cout<<l<<"=l  u="<<u<<"\n";
        fl=fn(l);
        fu=fn(u);
        cout<<i<<":: fn l ="<<fl<<" fn u ="<<fu<<"\n";
        if(fl<fu) b=u;
        else if(fl==fu)break;
        else a=l;
        i++;
    }
    cout<<"a ="<<a<<"b ="<<b;
    k++;
    return b;

}

void generate_fib()
{
    fib[0]=0;
    fib[1]=1;
    for(int i=2;i<51;i++) fib[i]=fib[i-1]+fib[i-2];
}


signed main(){

    double a,b,n,del;
    cin>>a>>b>>n>>del;
    generate_fib();
    double x=fibonacci(a,b,del,(int)n,0);

}