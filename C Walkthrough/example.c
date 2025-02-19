#include <stdio.h>

// Function to calculate factorial of a number
long factorial(int n);

int main(void) {
    int choice;

    // Show a simple menu to the user
    printf("Menu:\n");
    printf("1. Add two numbers\n");
    printf("2. Check if a number is odd or even\n");
    printf("3. Print the first 5 multiples of a number\n");
    printf("4. Calculate factorial\n");
    printf("Enter your choice (1-4): ");
    scanf("%d", &choice);

    if (choice == 1) {
        // Add two numbers
        int a, b;
        printf("Enter two integers: ");
        scanf("%d %d", &a, &b);
        printf("Sum = %d\n", a + b);

    } else if (choice == 2) {
        // Check odd or even
        int num;
        printf("Enter an integer: ");
        scanf("%d", &num);
        if (num % 2 == 0) {
            printf("%d is even.\n", num);
        } else {
            printf("%d is odd.\n", num);
        }

    } else if (choice == 3) {
        // Print first 5 multiples of a number using a for loop
        int n;
        printf("Enter an integer: ");
        scanf("%d", &n);
        printf("First 5 multiples of %d are: ", n);
        for (int i = 1; i <= 5; i++) {
            printf("%d ", n * i);
        }
        printf("\n");

    } else if (choice == 4) {
        // Calculate factorial
        int n;
        printf("Enter a positive integer to find its factorial: ");
        scanf("%d", &n);
        if (n < 0) {
            printf("Factorial of a negative number doesn't make sense!\n");
        } else {
            long fact = factorial(n);
            printf("Factorial of %d = %ld\n", n, fact);
        }
    } else {
        printf("Invalid choice. Please run the program again.\n");
    }

    return 0;
}

// Definition of factorial function
long factorial(int n) {
    // Factorial of 0 is 1
    if (n == 0) {
        return 1;
    }
    // Recursive approach
    return n * factorial(n - 1);
}
