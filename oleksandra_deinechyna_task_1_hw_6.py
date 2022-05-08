first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}

# Вариант 1, достаем с каждого словаря пары (items), так как это обьект items, то превращаем его в list,
# чтобы работать с ним. Через + суммируем наши пары в один список. Этот список пар превращаем в словарь через dict:
merged_dict1 = dict(list(first.items()) + list(second.items()) + list(third.items())
                    + list(fourth.items()) + list(fifth.items()))
print(merged_dict1)

# Вариант 2. Через update. Сначала создаем копию первого словаря.
# Потом добавляем значения остальных словарей по очереди.
merged_dict2 = first.copy()
merged_dict2.update(second)
merged_dict2.update(third)
merged_dict2.update(fourth)
merged_dict2.update(fifth)
print(merged_dict2)

# Вариант 3. Через цикл for: Из каждого словаря его элементы добавляем в новый словарь merged_dict3
merged_dict3 = {}
for key, value in first.items():
    merged_dict3[key] = value
for key, value in second.items():
    merged_dict3[key] = value
for key, value in third.items():
    merged_dict3[key] = value
for key, value in fourth.items():
    merged_dict3[key] = value
for key, value in fifth.items():
    merged_dict3[key] = value
print(merged_dict3)


# Вариант 4: попробовала вариант 3 сделать через функцию, но что-то короче не получилось, или я что-то не так делаю:
def merging_dicts(dicts):
    for k, v in dicts.items():
        merged_dict4[k] = v
    return merged_dict4


merged_dict4 = {}
merged_dict4 = merging_dicts(first)
merged_dict4 = merging_dicts(second)
merged_dict4 = merging_dicts(third)
merged_dict4 = merging_dicts(fourth)
merged_dict4 = merging_dicts(fifth)

print(merged_dict4)


# Вариант 5 для Python 3.9 и выше, но у меня 3.8:
# merged_dict = first | second | third | fourth | fifth


'''
сложить словари в один.
использовать for и dict methods.
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
'''
