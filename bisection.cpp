#include<bits/stdc++.h>
using namespace std;

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

double bisection(double a,double b,double del){
    double l,u,fl,fu;
    int i=1;
    while(b-a>del&&i<18){
        cout<<a<<"=a   b="<<b<<"\n";
        l= (b+a -del)/2;
        u= (b+a +del)/2;
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
    return b;

}


signed main(){

    double a,b,del;
    cin>>a>>b>>del;
    double x=bisection(a,b,del);

}