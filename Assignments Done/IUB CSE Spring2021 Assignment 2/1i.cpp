#include <iostream>
#include<math.h>

using namespace std;

int checkIntOrFloat(double input);

int main()
{
    double input=0;
    while (input<101) 
    {
        cout << "Enter the number : \n";
        cin >> input;
        if (input>100) { return 0; }
        checkIntOrFloat(input);
    }
    return 0;
}


int checkIntOrFloat(double input)
{
   int absulate = abs(input);
   if (input<0) { absulate = absulate*(-1) ;}

   cout <<( (input==absulate)? "Integer\n" : "Floating Point Number\n")<<endl;
   return 0;
}

