#include <stdio.h>

int main(void) {
    int i;
    int j;
    printf("enter first number");
    scanf("%d", &i);
    printf("enter second number");


    scanf("%d", &j);

    if (i > j) {
        printf("first number is greater%d\n", i);
    } else {
        printf("second number is greater %d\n", j);
    }

    return 0;
}
