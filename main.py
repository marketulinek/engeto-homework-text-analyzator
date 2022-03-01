from task_template import TEXTS

# -------------------------------

separator = '-' * 40

users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

max_num_of_texts = len(TEXTS)

# -------------------------------

username = input('username: ')
password = input('password: ')

if not users.get(username) == password:

    print('unregistered user, terminating the program..')
    quit()

else:
    print(separator)
    print('Welcome to the app', username.title())
    print(f'We have {max_num_of_texts} texts to be analyzed.')
    print(separator)
    user_choice = input(f'Enter a number between 1 and {max_num_of_texts} to select: ')

    if not user_choice.isnumeric():

        print('entered value is not a number, terminating the program..')
        quit()

    elif int(user_choice) <= 0 or int(user_choice) > max_num_of_texts:

        print(f'entered number is not between 1 and {max_num_of_texts}, terminating the program..')
        quit()

    else:
        print(separator)
        print(TEXTS)
