#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void welcomeMessage();
void LMSmenu();
void menu();

typedef struct library
{
    char Bname[30];
    char Bauthor[30];
    char category[30];
    int ID;
    float price;
}library;

void addBook()
{
    library *s;
    FILE *fp;
    int n,i;
    printf("How many book(s) you want to add: ");
    scanf("%d",&n);
    s = (library*)calloc(n, sizeof(library));
    fp = fopen("My_library.txt","w");

    for(i=0;i<n;i++)
    {
        printf("Enter Book Id: ");
        scanf("%d",&s[i]);
        printf("Enter Book name: ");
        scanf("%[^\n]s",s[i].Bname);
        printf("Enter Book category: ");
        scanf("%[^\n]s",s[i].category);
        printf("Enter Book price: ");
        scanf("%f",&s[i].price);
        fwrite(&s[i],sizeof(library),1,fp);
        fclose(fp);

    }

}

void deleteBook();     // Delete from File
void searchBook();     // Search from File
void viewAllBooks()
{
    library s1;
    FILE *fp;
    fp = fopen("My_library.txt","r");
}                       // Print Everything from File.
void Lend();           // Ask which book to lend to whom,
                       // then, store lending info in a file,
                       // which can be printed. (Receipt)
void returnBook();     // check if returned within date. if not, fine.
void calcFines();

int main(void)
{
    welcomeMessage();
    menu();
    return 0;
}



void welcomeMessage()
{
    printf("\n\n\n\n\n");
    printf("\n\t\t\t =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
    printf("\n\t\t\t =                     LMS                   =");
    printf("\n\t\t\t =                     BY                    =");
    printf("\n\t\t\t =                Julfikar Sarker,           =");
    printf("\n\t\t\t =                  Mahia Mehrun             =");
    printf("\n\t\t\t =                   & Afridi                =");
    printf("\n\t\t\t =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
    printf("\n\n");
    // getch();
}


void LMSmenu()
{
    printf("\n\t\t\t ##############################################");
    printf("\n\t\t\t ############                      ############");
    printf("\n\t\t\t ############       LMS Menu       ############");
    printf("\n\t\t\t ############                      ############");
    printf("\n\t\t\t ##############################################");
    printf("\n\t\t\t ----------------------------------------------\n");
    // Print stuff here
    printf("\n\t\t\t -----------------------------------------------");
}


void menu()
{
    int choice = 0;
    do
    {
        LMSmenu("MAIN MENU");
        printf("\n");
        printf("\n\n\t\t\t\t1.Add Books");
        printf("\n\t\t\t\t2.Delete Book");
        printf("\n\t\t\t\t3.Search Book");
        printf("\n\t\t\t\t4.View All Books");
        printf("\n\t\t\t\t5.Lend A Book");
        printf("\n\t\t\t\t0.Exit");
        printf("\n\n\n\t\t\t\tEnter choice => ");

        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            addBook();
            break;
        case 2:
            deleteBook();
            break;
        case 3:
            searchBook();
            break;
        case 4:
            viewAllBooks();
            break;
        case 5:
            Lend();
            break;
        case 6:
        case 0:
            printf("\n\n\n\t\t\t\t\tExiting LMS\n\n\n\n\n");
            exit(1);
            break;
        default:
            printf("\n\n\n\t\t\t INVALID INPUT, Go home you're Drunk");
        }
    }
    while(choice!=0);
}
