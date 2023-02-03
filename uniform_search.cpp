#include<bits/stdc++.h>
using namespace std;
int it;
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

double uni_search(double a,double b,int k){
    it++;
    cout<<" a = "<<a<<" b = "<<b<<" f(a) = "<<fn(a)<<endl;
    
    if((b-a)<0.001||it>=20) return a;
    double del = (b-a)/(k+1);
    double i,mv=fn(a),mi=a;
    i=a;
    while(i<b){
        i+=del;
        if(fn(i)<mv){
            mv=fn(i);
            mi=i;
        }
    }
    if(mi==a) return uni_search(a,a+del,k);
    else if(mi==b) return uni_search(b-del,b,k);
    return uni_search(mi-del,mi+del,k);

}


signed main(){

    double a,b,k;
    cin>>a>>b>>k;
    it=0;
    double x=uni_search(a,b,int(k));

}