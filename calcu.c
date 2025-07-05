#include<stdio.h>
int main(void){
int i;
int n;
int ap[n];

printf("enter the number of elements you want in array %d\n");
scanf("%d/n",n);
for(i=0; i<n ; i++){
    scanf("%d\n", ap[n]);

}
int max = ap[0];

for(i=0; i<n; i++){
    if (ap[i]>max){
        max = ap[i];
    };
printf("the largest number in arrray is =%d\n", max);
}
}