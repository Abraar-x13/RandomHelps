#include <iostream> 
#include <math.h> 
using namespace std; 

int main()
{
    float i = 0.25;
    float sum = 0;
    
    cout << "Series : ";
       while(i<5.20)
        {
            cout<< i ;
            if (i!=5) { cout<< " + ";}
            else {cout << " \n ";}
            sum = sum + i;
            i+=0.25;
        }
        cout << "Sum : ";
        cout<< sum ;
                
        return 0;
}
