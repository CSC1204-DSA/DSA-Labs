#include <stdio.h>

// Function prototype (declaration)
// This tells the compiler about the function before main().
int square(int x);

int main(void) {
    int num = 5;
    
    // Call the custom function
    int result = square(num);
    
    printf("The square of %d is %d\n", num, result);
    return 0;
}

// Function definition
// This function takes an integer and returns its square.
int square(int x) {
    return x * x;
}
