/*Asiignment 7 for Sayma Sultana Chowdhury ma'am
Evaluate A Postfix Expression*/
/* Student registration no : 2019831076 */

#include <stdio.h>
#include <ctype.h>

#define MAXSTACK 100 
#define POSTFIXSIZE 100 
int stack[MAXSTACK];
int top = -1; 

void push(int item);
int pop();
void EvalPostfix(char postfix[]);


int main(void)
{

    int i;
    char postfix[POSTFIXSIZE];
    printf(" \nEnter postfix expression,\npress right parenthesis ')' to end expression : ");


    for (i = 0; i <= POSTFIXSIZE - 1; i++) {
        scanf("%c", &postfix[i]);

        if (postfix[i] == ')')
        {
            break;
        } 
    }

    EvalPostfix(postfix);

    return 0;
}



void push(int item)
{

    if (top >= MAXSTACK - 1) 
    {
        printf("Stack over flow");
        return;
    }
    else 
    {
        top = top + 1;
        stack[top] = item;
    }
}

int pop()
{
    int item;
    if (top < 0) {
        printf("stack under flow");
    }
    else {
        item = stack[top];
        top = top - 1;
        return item;
    }
}


void EvalPostfix(char postfix[])
{

    int i,val,A,B;
    char ch;

    /* evaluate postfix expression */
    for (i = 0; postfix[i] != ')'; i++) 
    {
        ch = postfix[i];

        if (isdigit(ch)) 
        {   
            /*ch - '0' is used for getting digit rather than ASCII code of digit */
            push(ch - '0');
        }
        else if (ch == '+' || ch == '-' || ch == '*' || ch == '/') 
        {
            A = pop();
            B = pop();

            switch (ch)
            {
            case '*':
                val = B * A;
                break;
            case '/':
                val = B / A;
                break;
            case '+':
                val = B + A;
                break;
            case '-':
                val = B - A;
                break;
            } 

            push(val);
        }
    }
    printf(" \n Result : %d \n", pop());
}