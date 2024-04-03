# Que63:-Write a Python program to returns sum of all divisors of a number

# Ans:-

number = int(input("Enter a number: "))

divisor_sum = 0

for i in range(1, number + 1):
    if number % i == 0:
        divisor_sum += i

print("Sum of divisors of", divisor_sum)
