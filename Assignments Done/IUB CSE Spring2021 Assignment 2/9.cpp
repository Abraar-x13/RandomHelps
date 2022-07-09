#include <iostream>
#include<string.h>
using namespace std;

int main()
{
    char string1[100];
    int i, length;
    bool isPalindrome = false;
    
    cout << "Enter Number: ";
    cin >> string1;
    
    length = strlen(string1);
    
    for(i=0;i < length ;i++)
    {
        if(string1[i] != string1[length-i-1]) { isPalindrome = true; break; }
    }
    
    if (isPalindrome) { cout << "Not Symetric" << endl; }    
    else { cout << "Symetric" << endl; }

    return 0;
}
