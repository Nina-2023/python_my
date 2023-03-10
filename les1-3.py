number = int(input('Пожалуйста, введите номер: '))

n = number
nn = number * 10 + number
nnn = number * 100 + nn
sum = n + nn + nnn
print(f'The sum of {n}, {nn}, and {nnn} is {sum}')