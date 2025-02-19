#include <stdio.h>

int main(void) {
    int a = 10;
    int b = 3;

    // Addition
    int sum = a + b;
    // Subtraction
    int difference = a - b;
    // Multiplication
    int product = a * b;
    // Division
    int quotient = a / b;
    // Modulus (remainder of division)
    int remainder = a % b;

    printf("a = %d, b = %d\n", a, b);
    printf("a + b = %d\n", sum);
    printf("a - b = %d\n", difference);
    printf("a * b = %d\n", product);
    printf("a / b = %d (integer division)\n", quotient);
    printf("a %% b = %d\n", remainder);

    return 0;
}
