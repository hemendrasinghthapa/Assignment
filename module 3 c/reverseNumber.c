#include <stdio.h>

int main() {
	123
	5
  int n, reverse = 0, remainder;
  printf("Enter an number: ");
  scanf("%d", &n);
  while (n != 0) {
    remainder = n % 10;
    reverse = reverse * 10 + remainder;
    n =n/10;
  }
  printf("Reversed number = %d", reverse);
}