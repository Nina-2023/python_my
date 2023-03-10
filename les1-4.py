# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = int(input('Пожалуйста, введите положительное число: '))

max_digit = 0

while number > 0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number //= 10

print(f'The largest digit in the number is {max_digit}')