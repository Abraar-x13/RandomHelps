/*Asiignment 8 for Sayma Sultana Chowdhury ma'am
Convert a Infix expression to Postfix expression*/
/* Student registration no : 2019831076 */

#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>

#define SIZE 100
char stack[SIZE];
int top = -1;

void push(char item);
char pop();
int is_operator(char symbol);
int precedence(char symbol);


void InfixToPostfix(char infix_exp[], char postfix_exp[])
{ 
	int i, j;
	char item,x;

	push('(');
	strcat(infix_exp,")");

	i=0;
	j=0;
	item=infix_exp[i];

	while(item != '\0')
	{
		if(item == '(')
		{
			push(item);
		}
		else if( isdigit(item) || isalpha(item))
		{
			postfix_exp[j] = item;              /* add operand symbol to postfix expr */
			j++;
		}
		else if(is_operator(item) == 1)        /* means symbol is operator */
		{
			x=pop();
			while(is_operator(x) == 1 && precedence(x)>= precedence(item))
			{
				postfix_exp[j] = x;                  /* so pop all higher precendence operator and */
				j++;
				x = pop();                       /* add them to postfix expresion */
			}
			push(x);
			/* because just above while loop will terminate we have
			oppped one extra item
			for which condition fails and loop terminates, so that one*/

			push(item);                 /* push current oprerator symbol onto stack */
		}
		else if(item == ')')         /* if current symbol is ')' then */
		{
			x = pop();                   /* pop and keep popping until */
			while(x != '(')                /* '(' encounterd */
			{
				postfix_exp[j] = x;
				j++;
				x = pop();
			}
		}
		else
		{ 
			printf("\nInvalid infix Expression.\n");
			getchar();
			exit(1);
		}
		i++;


		item = infix_exp[i]; /* go to next symbol of infix expression */
	} /* while loop ends here */
	
		if(top>0)
		{
			printf("\nInvalid infix Expression.\n");
			getchar();
			exit(1);
		}



	postfix_exp[j] = '\0'; /* add sentinel else puts() fucntion */
	/* will print entire postfix[] array upto SIZE */

}


int main()
{
	char infix[SIZE], postfix[SIZE];

	printf("\nEnter Infix expression : ");
	gets(infix);

	InfixToPostfix(infix,postfix);  
	printf("Postfix Expression: ");
	puts(postfix); 

	return 0;
}


void push(char item)
{
	if(top >= SIZE-1)
	{
		printf("\nStack Overflow.");
	}
	else
	{
		top = top+1;
		stack[top] = item;
	}
}

char pop()
{
	char item ;

	if(top <0)
	{
		printf("stack under flow: invalid infix expression");
		getchar();
		/* underflow may occur for invalid expression */
		/* where ( and ) are not matched */
		exit(1);
	}
	else
	{
		item = stack[top];
		top = top-1;
		return(item);
	}
}

int is_operator(char symbol)
{
	if(symbol == '^' || symbol == '*' || symbol == '/' || symbol == '+' || symbol =='-')
	{
		return 1;
	}
	else
	{
	return 0;
	}
}


int precedence(char symbol)
{
	/* define fucntion that is used to assign precendence to operator.
    * Here ^ denotes exponent operator.
    * In this fucntion we assume that higher integer value
    * means higher precendence */
    
	if(symbol == '^')/* exponent operator, highest precedence*/
	{
		return(3);
	}
	else if(symbol == '*' || symbol == '/')
	{
		return(2);
	}
	else if(symbol == '+' || symbol == '-')          /* lowest precedence */
	{
		return(1);
	}
	else
	{
		return(0);
	}
}
/*   
FOR MY HELP :
Algorithm to convert Infix To Postfix
Let, X is an arithmetic expression written in infix notation. This algorithm finds the equivalent postfix expression Y.

1.Push “(“onto Stack, and add “)” to the end of X.
2.Scan X from left to right and repeat Step 3 to 6 for each element of X until the Stack is empty.
3.If an operand is encountered, add it to Y.
4.If a left parenthesis is encountered, push it onto Stack.
5.If an operator is encountered ,then:
5a.Repeatedly pop from Stack and add to Y each operator (on the top of Stack) which has the same precedence as or higher precedence than operator.
5b.Add operator to Stack.
[End of If]
6.If a right parenthesis is encountered ,then:
6a.Repeatedly pop from Stack and add to Y each operator (on the top of Stack) until a left parenthesis is encountered.
6b.Remove the left Parenthesis.
[End of If]
[End of If]
7.END.
*/
