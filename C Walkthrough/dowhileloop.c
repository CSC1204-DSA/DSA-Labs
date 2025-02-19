#include <stdio.h>

int main(void) {
    int count = 0;
    
    // do...while loop always executes at least once
    do {
        printf("Loop iteration: %d\n", count);
        count++;
    } while (count < 3);  // condition is checked after each iteration

    return 0;
}
