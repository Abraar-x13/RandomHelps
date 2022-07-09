#include <iostream> 
#include <math.h> 
using namespace std; 

int main()
{
    int i = 2;
    int sum = 0;
    
    cout << "Series : ";
       while(i<101)
        {
            cout<< i ;
            if (i!=100) { cout<< " + ";}
            else {cout << " \n ";}
            sum = sum + i;
            i+=2;
        }
        cout << "Sum : ";
        cout<< sum ;
                
        return 0;
}
