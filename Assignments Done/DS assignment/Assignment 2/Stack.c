/*Asiignment 6 for Sayma Sultana Chowdhury ma'am
Stack Implementation
Push() function
Pop() function*/
/* Student registration no : 2019831076 */

#include <stdio.h>
#include<stdlib.h>

int MAXSIZE = 10;       
int stack[10];     
int top = -1;            

int isempty(); 
int isfull();


int pop() 
{
   int data;
   if(!isempty()) 
   {
      data = stack[top];
      top = top - 1;   
      return data;
   } 
   else {
      printf("Can't pop, Stack is empty.\n");
   }
}

int push(int data) 
{

   if(!isfull()) 
   {
      top = top + 1;   
      stack[top] = data;
   } else {
      printf("Can't push, Stack is full.\n");
   }
}

int main() {
   int x,y,z;
   while(1)
   {
      printf("Press 1 to push data, 2 to pop, 0 to exit \n");
      scanf("%d", &x);
      if (x==0) { break; }
      else if (x=1) 
      {
         int z = scanf("%d", &y);
         push(z);
      }
      else if (x=2)
      {
         pop();
      }
      else {printf("Invalid input\n");}

   }

   return 0;
}




int isempty() 
{

   if(top == -1)
      return 1;
   else
      return 0;
}
int isfull()
{

   if(top == MAXSIZE)
      return 1;
   else
      return 0;
}