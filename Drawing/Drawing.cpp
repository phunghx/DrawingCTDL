#include "graphics.h"
#include <dos.h>
#include <stdio.h>
#include <conio.h>

int main()
{
    int i, j = 0;
    char ini[] = "C:\\TURBOC3\\BGI";
    initgraph();

    char s1[] = "Press any key to view the moving car";
    outtextxy(25, 240, s1);

    
    for (i = 0; i <= 420; i = i + 10, j++)
    {
        rectangle(50 + i, 275, 150 + i, 400);
        rectangle(150 + i, 350, 200 + i, 400);
        circle(75 + i, 410, 10);
        circle(175 + i, 410, 10);
        setcolor(j);
        Sleep(10);

        if (i == 420)
            break;
        system("cls");

    }
    return 0;
}