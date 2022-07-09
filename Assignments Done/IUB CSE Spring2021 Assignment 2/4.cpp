//Question had 4 different type of examples, I implemented all in one program.

#include <iostream>

using namespace std;
int starHalfPyramid(int rows);
int starHalfPyramid_inverted(int rows);
int increasingRowNumber_HalfPyramid(int rows);
int notIncreasingRowNumber_HalfPyramid(int rows);

int main()
{
    int rows;

    cout << "Enter number of rows: ";
    cin >> rows;
    cout << "\n";
    cout << "Pattern 1 - Half Pyramid with Stars : \n";
    starHalfPyramid(rows);
    cout << "\n \n \n";
    cout << "Pattern 2 - Inverted Half Pyramid with Stars : \n";
    starHalfPyramid_inverted(rows);
    cout << "\n \n \n";
    cout << "Pattern 3 - Half Pyramid with number increasing in every column : \n";
    increasingRowNumber_HalfPyramid(rows);
    cout << "\n \n \n";
    cout << "Pattern 4 - Half Pyramid with number increasing in every row : \n";
    notIncreasingRowNumber_HalfPyramid(rows);
    cout << "\n \n \n";

    return 0;
}


int starHalfPyramid(int rows)
{
    for(int i = 1; i <= rows; ++i)
    {
        for(int j = 1; j <= i; ++j)
        {
            cout << "* ";
        }
        cout << "\n";
    }
    return 0;
}

int starHalfPyramid_inverted(int rows)
{
    for(int i = rows; i >= 1; --i)
    {
        for(int j = 1; j <= i; ++j)
        {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}

int increasingRowNumber_HalfPyramid(int rows)
{
    for(int i = 1; i <= rows; ++i)
    {
        for(int j = 1; j <= i; ++j)
        {
            cout << j << " ";
        }
        cout << "\n";
    }
    return 0;
}

int notIncreasingRowNumber_HalfPyramid(int rows)
{
    for(int i = 1; i <= rows; ++i)
    {
        for(int j = 1; j <= i; ++j)
        {
            cout << i << " ";
        }
        cout << "\n";
    }
    return 0;
}
