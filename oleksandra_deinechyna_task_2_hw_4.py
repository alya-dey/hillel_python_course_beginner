numbers_of_letters = {}
string: str = input('Введите вашу строку: ')
#Прогоняем каждую букву строки через цикл for
# (поскольку строка это последовательность символов, то делить строку на символы на надо):
for letter in string:
    #Словарь[key] = value (добавляем +1 каждый раз, когда цикл for находит ту же букву в строке):
    numbers_of_letters[letter] = numbers_of_letters.get(letter, 0)+1
print(numbers_of_letters, end='\n'+'_'*30+'\n')

# ВАРИАНТ №2 (увидела модуль collections, пока делала другие задачи):
import collections

numbers_of_letters_2 = collections.Counter()
for letter in string:
    numbers_of_letters_2[letter] +=1
print(dict(numbers_of_letters_2))

'''
Тема Dict
Написать программу, которая подсчитывает количество символов в строке
и формирует dict в котором key = буква, value= количество их в слове:
Входная строка : 'Hillel school'
Результат :  {'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}
'''
