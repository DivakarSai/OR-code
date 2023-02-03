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
    return 2*exf(x,6)+3*exf(x,4)-12*x;
}
double df(double x){
    return 12*exf(x,5)+12*exf(x,3)-12;
}
double ddf(double x){
    return 60*exf(x,4)+36*exf(x,2);
}

void newton(double l0,double del=0.01){
    double l1 = l0- (df(l0)/ddf(l0));
    int i=1;
    while(abs(l1-l0)>del&&i<=30){
        cout<<"l0= "<<l0<<" l1 = "<<l1<<endl;
        l0=l1;
        l1 = l0- (df(l0)/ddf(l0));
        i++;
        
    }
    cout<<"l0= "<<l0<<" l1 = "<<l1<<endl;
    
}


signed main(){

    double l;
    cin>>l;
    newton(l);
    return 0;
    

}