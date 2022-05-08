my_dict = {2: 'two', 4: 'four', 1: 'one', 5: 'five', 3: 'three'}
# Через функцию sorted создаем отсортированный список элементов словаря. Его превращаем обратно в словарь через dict:
my_dict_sorted = dict(sorted(my_dict.items()))
print(my_dict)
print(my_dict_sorted)

'''
отсортировать словарь по ключам
'''
