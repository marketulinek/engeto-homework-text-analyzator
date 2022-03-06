from task_template import TEXTS

users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}
separator = '-' * 40
number_of_texts = len(TEXTS)

# -------------------------------
#            PROGRAM
# -------------------------------

username = input('username: ')
password = input('password: ')

if not users.get(username) == password:

    print('unregistered user, terminating the program..')
    quit()

else:
    print(separator)
    print('Welcome to the app', username.title())
    print(f'We have {number_of_texts} texts to be analyzed.')
    print(separator)
    user_choice = input(f'Enter a number between 1 and {number_of_texts} to select: ')

    if not user_choice.isnumeric():

        print('entered value is not a number, terminating the program..')
        quit()

    elif int(user_choice) <= 0 or int(user_choice) > number_of_texts:

        print(f'entered number is not between 1 and {number_of_texts}, terminating the program..')
        quit()

    else:
        text_stats = {
            'titlecase': 0,
            'uppercase': 0,
            'lowercase': 0,
            'numeric_strings': 0,
            'sum_of_all_numbers': 0
        }
        chosen_text = TEXTS[int(user_choice)-1].strip().replace('\n', ' ').replace(',', '').replace('.', '')
        list_of_words = chosen_text.split(' ')

        for word in list_of_words:

            if word.istitle():
                text_stats['titlecase'] += 1

            if word.isupper():
                text_stats['uppercase'] += 1
                # TODO '30N' from TEXT[1] got here but shouldn't

            if word.islower():
                text_stats['lowercase'] += 1

            if word.isnumeric():
                text_stats['numeric_strings'] += 1
                text_stats['sum_of_all_numbers'] += int(word)

        print(separator)
        print(f'There are {len(list_of_words)} words in the selected text.')
        print(f'There are {text_stats["titlecase"]} titlecase words.')
        print(f'There are {text_stats["uppercase"]} uppercase words.')
        print(f'There are {text_stats["lowercase"]} lowercase words.')
        print(f'There are {text_stats["numeric_strings"]} numeric strings.')
        print(f'The sum of all the numbers {text_stats["sum_of_all_numbers"]}.')
        print(separator)
