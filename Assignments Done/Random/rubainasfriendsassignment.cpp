#include <iostream>

void lyrics();
void printT();

int main(void)
{
    std::cout << "Answer of Q1:" << '\n';
    lyrics();
    std::cout << "Answer of Q2:" << '\n';
    printT();
    return 0;
}

// Funtion to print four lines of "But Not For Me" by "Chet Baker"
void lyrics()
{
    std::cout << "Lyrics of 'But Not For Me' by Chet Baker-" << '\n';
    std::cout << "They're writing songs of love," << '\n';
    std::cout << "but not for me." << '\n';
    std::cout << "A lucky star's above," << '\n';
    std::cout << "but not for me." << '\n';
    std::cout <<std::endl;
}

// Funtion to print first letter of my last name - "T"
void printT()
{
    int y = 6, yh = y/2, x = (y-1);
	for (int i=0; i<y; i++)
    {
		for (int j=0; j<x; j++)
        {
            if (i == 0) { std::cout <<" *";}
            else if (j == yh){ std::cout <<"  *"; }
			else { std::cout <<" "; }
		}
		std::cout <<std::endl;
	}
}
