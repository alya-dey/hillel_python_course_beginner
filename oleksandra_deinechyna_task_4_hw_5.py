methods = [f for f in dir(set) if not f.startswith("__")]
print(methods)

"""
Если вводить имя функции будет пользователь через инпут (function = type(input('Enter function to show all methods: ')),
то dir будет считывать название функции как строку. Превратить str в type не получилось(
"""

'''
Задача: написать программу которая будет создавать список методов из доступных методов питон объектов. Под доступными подразумевается
методы без подчеркиваний. Фунции dir()
т.е для объекта set должен быть список методов
['add',
 'clear',
 'copy',
 'difference',
 'discard',
 'intersection',
 'isdisjoint',
 'issubset',
 'issuperset',
 'pop',
 'remove',
 'union',
 'update']
'''