#include <iostream>
#include<math.h>

using namespace std;
int checkInput(char input);

int main()
{
    char input;
    while (1) 
    {
        cout << "Enter a character: ";
        cin >> input;
        if (input >= 65 && input <= 90 || input >= 97 && input <= 122 || input >= 48 && input <= 57) 
            { checkInput(input); }
        else { return 0; }
    }
}


int checkInput(char input)
{
    if(input >= 65 && input <= 90)
        cout << "Upper-case character\n";
    else if(input >= 97 && input <= 122)
        cout << "Lower-case character\n";
    else if(input >= 48 && input <= 57)
        cout << "Digit\n";
    return 0;
}
