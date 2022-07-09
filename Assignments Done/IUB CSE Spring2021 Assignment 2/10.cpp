//The question said binary but output had octal so I implemented both

#include <iostream>
#include<string.h>
using namespace std;

int convertToBase_2(int num);
int convertToBase_8(int num);

int main(void)
{
    int num;

    cout<<"Enter a number: ";
    cin>>num;
    
    cout<<"The number in Decimal : ";
    cout<<num;
    cout<<"\n";
    cout<<"The number in Binary : ";
    convertToBase_2(num);
    cout<<"\n";
    cout<<"The number in Octal : ";
    convertToBase_8(num);

    return 0;
}


int convertToBase_2(int num)
{
    int base = 2;
    int rem;

    if (num == 0) { return 0; }

    else
    {
        rem = num % base;       
        convertToBase_2(num/base);    
    }
    
    cout<<rem;
    return 0;

}

int convertToBase_8(int num)
{    
    int base = 8;
    int rem;

    if (num == 0) { return 0; }

    else
    {
        rem = num % base;     
        convertToBase_8(num/base);      

    }
    
    cout<<rem;
    return 0;

}
