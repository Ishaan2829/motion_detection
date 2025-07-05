#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Enter the number of array elements: ");
    scanf("%d", &n);

    int *ap = malloc(n * sizeof(int));  // ✅ Dynamic allocation

    if (ap == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    printf("Enter the array elements:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &ap[i]);
    }

    printf("Array elements are:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", ap[i]);
    }

    free(ap);  // ✅ Free dynamically allocated memory
    return 0;
}
