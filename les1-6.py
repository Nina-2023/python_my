# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
revenue = int(input('введите выручку компании: '))
cost = int(input('введите расходы компании: '))

profit = revenue - cost

if profit > 0:
    rentability = profit / revenue
    print(f'рентабельность компании  {rentability:.2f}')

    employees = int(input('введите количество сотрудников: '))
    profit_per_employee = profit / employees
    print(f'Прибыль компании на одного работника {profit_per_employee:.2f}')