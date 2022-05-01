list_of_items: list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
# Через цикл while проверяем каждый элемент списка по очереди:
i = 0
while i < len(list_of_items):
    # Удаляем элемент списка, если он равен определенному значению:
    if list_of_items[i] == 'eg':
        del list_of_items[i]
    else:
        i += 1
print(list_of_items)


# Вариант №2 - покороче: пока в списке есть определенный элемент, удаляем его через remove:
list_of_items2: list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
item_for_del = 'eg'
while item_for_del in list_of_items2:
    list_of_items2.remove(item_for_del)
print(list_of_items2)


'''
Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.
Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
Результат: ['bear', 'milk']
'''