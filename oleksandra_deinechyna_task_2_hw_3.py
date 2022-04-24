user_name: str = input('Введите ваш никнейм ')
user_age = int(input('Введите ваш возраст '))
user_gender: str = input('Укажите ваш пол (М/Ж) ')

if user_name == 'Женя':
    print('Советую Вам посмотреть "TENET"')

elif 'admin' in user_name:
    print('Привет, повелитель!')
    if user_gender == 'М':
        if 10 <= user_age <= 14 or user_age > 30:
            print('Советую Вам посмотреть "Starwars" или "Мандалорец"')
        elif user_age < 10:
            print('Советую Вам посмотреть "TMNT"')
        else:
            print('Мне нечего вам посоветовать :(')
    elif user_gender == 'Ж':
        if user_age <= 16:
            print('Советую Вам посмотреть "Инсургент')
        elif 22 < user_age < 32:
            print('Советую Вам посмотреть "Трансформеры"')
        else:
            print('Мне нечего вам посоветовать :(')
    else:
        print('Вы неккоректно ввели пол')

elif user_name == 'Guido':
    print('Огромное спасибо!')
    if user_gender == 'М':
        if 10 <= user_age <= 14 or user_age >= 30:
            print('Советую Вам посмотреть "Starwars" или "Мандалорец"')
        elif user_age < 10:
            print('Советую Вам посмотреть "TMNT"')
        else:
            print('Мне нечего вам посоветовать :(')
    elif user_gender == 'Ж':
        if user_age <= 16:
            print('Советую Вам посмотреть "Инсургент')
        elif 22 <= user_age <= 32:
            print('Советую Вам посмотреть "Трансформеры"')
        else:
            print('Мне нечего вам посоветовать :(')
    else:
        print('Вы неккоректно ввели пол')

else:
    if user_gender == 'М':
        if 10 <= user_age <= 14 or user_age >= 30:
            print('Советую Вам посмотреть "Starwars" или "Мандалорец"')
        elif user_age < 10:
            print('Советую Вам посмотреть "TMNT"')
        else:
            print('Мне нечего вам посоветовать :(')
    elif user_gender == 'Ж':
        if user_age <= 16:
            print('Советую Вам посмотреть "Инсургент')
        elif 22 <= user_age <= 32:
            print('Советую Вам посмотреть "Трансформеры"')
        else:
            print('Мне нечего вам посоветовать :(')
    else:
        print('Вы неккоректно ввели пол')

"""
Сначала проверяем ник, потом пол, потом возраст.
Получилось, что 3 раза дублируются условия с полом и возрастом,
наверняка можно проверку по никнейму как-то сократить, но не 
нашла другого решения(
"""

