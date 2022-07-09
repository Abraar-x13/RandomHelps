#include <iostream>

using namespace std;

int getSum(string str);
int getAverage(string str);


int main()
{
    string Number;
    cout << "Enter Number : ";
    cin >> Number;
    cout << "\n";
    cout << "Sum     : ";
    getSum(Number);
    cout << "\n";
    cout << "Average : ";
    getAverage(Number);
    return 0;
}

int getSum(string str)
{
    float sum = 0;
 
    for (float i = 0; i < str.length(); i++)  { sum = sum + str[i] - 48; }
    cout << sum;
    return 0;
}

int getAverage(string str)
{
    float sum = 0;
 
    for (float i = 0; i < str.length(); i++) { sum = sum + str[i] - 48; }
    float Average = sum/str.length();
    cout << Average;
    
    return 0;
}
