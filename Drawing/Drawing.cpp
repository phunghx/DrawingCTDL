#include "graphics.h"
#include <dos.h>
#include <stdio.h>
#include <conio.h>

int main()
{
    int i, j = 0;
    initgraph();

    char s1[] = "Press any key to view the moving car";
    //outtextxy(25, 240, s1);

    drawText(100, 500, "Hello");
    drawText(200, 300, "H");

    _getch();
    
    int y = 5;
    for (i = 0; i <= 420; i = i + 2, j++)
    {
        rectangle(50 + i, 275+ i, 150 + i, 400+i);
        rectangle(150 + i, 350+i, 200 + i, 400+i);
        circle(75 + i, 410+i, 10);
        circle(175 + i, 410+i, 10);
        setcolor(j);
        Sleep(10);

        if (i == 420)
            break;
        system("cls");

    }
    return 0;
}