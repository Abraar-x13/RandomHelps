#include <iostream> 
#include <math.h> 

using namespace std; 
int checkPerfect(int n);

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    checkPerfect(n);
    return 0;
}

int checkPerfect(int n)
{
    int i=1,sum=0;
       while(i<n)
        {
            if(n%i==0){ sum+=i; }
            i++; 
        }

    if(sum==n) { cout << "Perfect\n"; }
    else { cout <<"Not Perfect\n"; }

    return 0;
}
