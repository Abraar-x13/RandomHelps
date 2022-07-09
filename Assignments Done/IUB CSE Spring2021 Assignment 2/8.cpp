#include <iostream> 
#include <math.h> 

using namespace std;
int primeInsecondNumange(int firstNum, int secondNum);

int main() 
{ 
    int firstNum; 
    int secondNum; 

    cin>>firstNum; 
    cin>>secondNum; 

    if (firstNum>secondNum) 
    {
        int temp;
        temp = firstNum;
        firstNum = secondNum;
        secondNum = temp;
    }

    primeInsecondNumange(firstNum, secondNum); 
  
    return 0; 
}

int primeInsecondNumange(int firstNum, int secondNum) 
{ 
    bool isPrime; 

    for (int i = firstNum; i <= secondNum; i++) 
    {
        if (i == 0 || i == 1) { continue; }

        isPrime = true; 
  
        for (int j = 2; j <= i / 2; ++j) 
        { 
            if (i % j == 0) { isPrime = false; break; } 
        } 
        if (isPrime == true) 
            cout << i << " "; 
    } 
    return 0;
} 
