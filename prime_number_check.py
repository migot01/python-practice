num = input('Enter a number: ')
num = int(num)
count = 0

if num > 1:
    for i in range(1, num+1):
        if num % i == 0:
            count += 1

if count == 2:
    print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')
            