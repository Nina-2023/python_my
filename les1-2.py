#Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
seconds = int(input('Пожалуйста, введите время в секундах: '))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))