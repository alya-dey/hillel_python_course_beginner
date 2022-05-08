schedule = {'monday': ['clean house', 'drive car', 'meet with freands'],
           'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
# Создаем переменную - количество наименований в списках, изначально она = 0:
number_of_tasks = 0
# Перебираем все значения словаря через values():
for value in schedule.values():
    # Через функцию isinstance проверяем, является ли это значение списком:
    if isinstance(value, list):
        # Если True, то прибавляем длину этого списка к переменной number_of_values:
        number_of_tasks += len(value)
print(number_of_tasks)





'''
Посчитать общее количество наименований в списке. И только в списках.
Example:
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
Результат: 6
'''
