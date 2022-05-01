password: str = input('Please enter your password: ')
password2: str = input('Please repeat your password: ')
while password2 != password:
    print('Passwords don\'t match.')
    password2: str = input('Please repeat your password: ')
    continue
else:
    print('Passwords match, thank you.')


'''
пользователь вводит пароль первый раз система запоминает и просит повторить пароль проверяет его если нет то просит повторить. А если совпал то сообщение.
'''