#include <stdio.h>

int main(void) {
    int num;

    printf("Enter numbers (0 to stop): ");
    scanf("%d", &num);

    // The loop continues as long as num != 0
    while (num != 0) {
        printf("You entered: %d\n", num);
        // Read the next number
        scanf("%d", &num);
    }

    printf("Exited the loop because you entered 0.\n");
    return 0;
}
