#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void fast(void); 


void rejection_sampling(int k)
{
   std::random_device rd;
   std::mt19937 gen(rd());
   std::uniform_real_distribution<> rng(-1, 1);
   rng(gen);
   while (k)
   {
      float x = rng(gen);
      float y = rng(gen);
      if (x*x+y*y < 1)
      {
         cout << x << " " <<y<< "\n"; k--;
      }
   }
}

void sqrt_dist(int k)
{
   std::random_device rd;
   std::mt19937 gen(rd());
   std::uniform_real_distribution<> rng(-1, 1);
   rng(gen);

   while (k)
   {
      float theta = rng(gen) * 2 * 3.14159;
      float r = sqrt(rng(gen));
      if(!isnan(r*cos(theta)))
      {
         cout << r*(cos(theta)) << " " << r*(sin(theta)) << "\n"; k--;
      }
   }
}


void sum_dist(int k)
{
   std::random_device rd;
   std::mt19937 gen(rd());
   std::uniform_real_distribution<> rng(-1, 1);
   rng(gen);

   while (k)
   {
      float theta = rng(gen) * 2 * 3.14159;
      float x1 = rng(gen);
      float x2 = rng(gen);
      float r = x1+x2;
      if(r>1) 
      {
         r = 2 - r;
      }
      if(!isnan(r*cos(theta)))
      {
         cout << r*(cos(theta)) << " " << r*(sin(theta)) << "\n"; k--;
      }
   }
}


void max_dist(int k)
{
   std::random_device rd;
   std::mt19937 gen(rd());
   std::uniform_real_distribution<> rng(-1, 1);
   rng(gen);

   while (k)
   {
      float theta = rng(gen) * 2 * 3.14159;
      float r = rng(gen);
      float x2 = rng(gen);
      if (x2>r)
      {
         r = x2;
      }
      if(!isnan(r*cos(theta)))
      {
         cout << r*(cos(theta)) << " " << r*(sin(theta)) << "\n"; k--;
      }
   }
}



int main(void) 
{
   fast();

   // cout<< -1 + static_cast <float> (rand()) / ( static_cast <float> (RAND_MAX/(1-(-1))))<<"\n";
   // cout << ((float) rand()/RAND_MAX) * 2 - 1 << endl;


   max_dist(50);


   return 0;
}


void fast(void) 
{
   std::ios::sync_with_stdio(false); 
   cin.tie(NULL);
}