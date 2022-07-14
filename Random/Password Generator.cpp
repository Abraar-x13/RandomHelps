#include "/Users/abraar/Code Stuff/VS Code Stuff/VS-Code-GitHub/CPP/stdc++.h"
// #include <bits/stdc++.h>
#include <chrono>
#include <random>
using namespace std;
using u32 = uint_least32_t;
using engine = std::mt19937;

int get_random_number(int min, int max);

int main(void)
{
    char letters[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                      'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
                      'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    char numbers[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    char symbols[] = {'!', '#', '$', '%', '&', '(', ')', '*', '+'};

    string pass = "";

    for (int i = 0; i < 13; i++)
    {
        // Generate a random number between 0 and 3
        int num = get_random_number(0, 3);
        if (num == 0)
        {
            int idx = get_random_number(0, (sizeof(letters) / sizeof(letters[0])) - 1);
            pass += letters[idx];
        }
        if (i % 11 == 0)
        {
            pass += "MeR";
        }
        else if (num == 1)
        {
            int idx = get_random_number(0, (sizeof(numbers) / sizeof(numbers[0])) - 1);
            pass += numbers[idx];
        }
        else if (num == 2)
        {
            int idx = get_random_number(0, (sizeof(symbols) / sizeof(symbols[0])) - 1);
            pass += symbols[idx];
        }
    }

    cout << pass << endl;
}

int get_random_number(int min, int max)
{
    std::random_device os_seed;
    const u32 seed = os_seed();

    engine generator(seed);
    std::uniform_int_distribution<u32> distribute(min, max);

    for (int repetition = 0; repetition < 10; ++repetition)
    {
        const u32 random_number = distribute(generator);
        if (random_number >= min && random_number <= max)
        {
            return random_number;
        }
    }
    return 0;
}