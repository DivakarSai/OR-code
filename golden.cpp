#include<bits/stdc++.h>
using namespace std;

double f(double x){
	double ans = (x*x)+ (exp(-1*x));
	return ans;
}

signed main(){

	double del,a,b,lb,mu,fl,fu;
	cin>>a>>b>>del;

	lb = a+ 0.382*(b-a);
	mu = a+ 0.618*(b-a);
	fl = f(lb);
	fu =f(mu);
	int i=0;
	
	while(b-a>=del){
        cout<<"-----------------------------------------------------------------"<<"\n";
        cout<<fl<<"    "<<fu<<"\n";
        
		cout<<"at the step no"<<i++<<"  a="<<a<<"  b="<<b<<"\n";
		cout<<lb<<" "<<mu<<endl;
		if(fl>fu){
			a=lb;
			lb=mu;
			fl=fu;
			mu=a+ 0.618*(b-a);
			fu=f(mu);
			continue;
		}
		else{
			b=mu;
			mu=lb;
			fu=fl;
			lb=lb = a+ 0.382*(b-a);
			fl=f(lb);
			continue;
		}
	}
    cout<<"-----------------------------------------------------------------"<<"\n";
	cout<<"a="<<a<<" b ="<<b<<"\n";

}
