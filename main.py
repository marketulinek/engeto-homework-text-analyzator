separator = '-' * 40

users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# -------------------------------

username = input('username: ')
password = input('password: ')

if not users.get(username) == password:

    print('unregistered user, terminating the program..')
    quit()

else:
    print(separator)
    print('Welcome to the app', username.title())
    print('We have 3 texts to be analyzed.')
    print(separator)
    user_choice = input('Enter a number between 1 and 3 to select: ')

    if not user_choice.isnumeric():

        print('entered value is not a number, terminating the program..')
        quit()

    elif user_choice not in range(1, 4):  # or [1,2,3] or not in TEXTS var

        print('entered number is not between 1 and 3, terminating the program..')
        quit()

    else:
        print(separator)
