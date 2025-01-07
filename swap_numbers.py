num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

print('Before swapping: num1 =', num1, 'num2 =', num2)

# swapping two numbers using a temporary variable
# temp = num1
# num1 = num2
# num2 = temp

# swapping two numbers without using a temporary variable
num1, num2 = num2, num1

print('After swapping: num1 =', num1, 'num2 =', num2)


