students_marks = {'id1':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
},
'id2':
{
'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}
},
'id3':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
}
}

# Создаем новый пустой словарь:
students_marks_new = {}
# Через dict comprehension добавляем в новый словарь ключ и значение из первого словаря,
# проверяя, нет ли уже такого значения (используя функцию dict.values())
[students_marks_new.update({k: v}) for k, v in students_marks.items() if v not in students_marks_new.values()]
print(students_marks)
print(students_marks_new)

'''
Удалить дубликаты из dictionary
пример
Before :
{'id1':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
},
'id2':
{
'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}
},
'id3':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
}
}

After:
{'id1':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
},
'id2':
{
'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}
}

'''
