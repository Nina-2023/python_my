# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
revenue = int(input('введите выручку компании: '))
cost = int(input('введите расходы компании: '))

if revenue > cost:
    print('компания получает прибыль!')
elif revenue < cost:
    print('компания работает в убыток!')
else:
    print('компания безубыточна!')