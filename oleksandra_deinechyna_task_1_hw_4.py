string: str = input('Введите вашу строку: ')
if len(string) < 2:
    print('Ваша строка слишком короткая - %s'%string)
else:
    print(string[:2]+string[-2:])


'''
Срезы и условие if.
написать программку которая будет состоять из первых двух и последних символов предоставленной строки.
Если длинна строки меньше двух символов напечатать строку типа.
'Ваша строка слишком короткая - СТРОКА ' . Через метод форматирования строк с %.
Входная строка : 'Hillel school'
Результат1 : 'Hiol' 
или
Результат2 : 'Ваша строка слишком короткая - и ваша строка'
'''