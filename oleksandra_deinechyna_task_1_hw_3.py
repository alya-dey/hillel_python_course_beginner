user_age = input('Please enter your age ')
if not user_age.isdigit():
    print('Please enter your age in number format')
elif int(user_age) == 21:
    print('You should visit Holland.')
elif int(user_age) > 21:
    print('You should visit Vietnam.')
else:
    print('Travel everywhere')
