user_name: str = input('Please enter your name: ')
print('{} {}'.format(user_name.upper(), user_name.lower()))

# Вариант короче, без .format():
print(user_name.upper(), user_name.lower())

'''
Пользователь водит свое имя.
Возвращается тектс в БОЛЬШОМ и маленьком регистре. Использовать ' '.format().
Для вставки аргументов в текст.
Входные данные: Apollo
Результат: APPOLLO apollo
'''
