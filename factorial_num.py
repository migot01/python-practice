num = input('Enter a number: ')
num = int(num)
factorial = 1

if num < 0:
    print('Factorial is not defined for negative numbers.')
elif num == 0:
    print('Factorial of 0 is 1.')
else:
    for i in range(1, num+1):
        factorial *= i
    print('Factorial of', num, 'is', factorial)

