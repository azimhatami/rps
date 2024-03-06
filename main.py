import random
import os

choices = [
    'r',
    'p',
    's',
]

choice_meaning = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors',
}


def clear_screen():
    os.system('clear')

def welcome_message(name):
    print(f'Hi {name}, welcome to Rock, Paper, Scissors game!!!', '\n')
    print(f'Let\'s Gooo {name}')
    print('\n', '-' * 18, '\n')


def get_user_choice(name):
    user_choice = input(f'{name} Select from Rock, Paper, Scissors: [r/p/s] ')

    while user_choice not in choices:
        print('Sorry, try again.')
        user_choice = input(f'{name} Select from Rock, Paper, Scissors: [r/p/s] ')
    return user_choice

def get_ai_choice():
    ai_choice = random.choice(choices)
    return ai_choice

def find_winner(user_choice, ai_choice, name):
    if user_choice == ai_choice:
        return 'Tie'
    # r > s - p > r - s > p
    elif (user_choice == 'r' and ai_choice == 's') or \
         (user_choice == 'p' and ai_choice == 'r') or \
         (user_choice == 's' and ai_choice == 'p'):
        return f'{name} winnn!!!'
    else:
        return 'Ai wonnn!!!'


if __name__ == '__main__':
    clear_screen()
    name = input('Please enter a name: ').capitalize()
    welcome_message(name)
    while True:
        user_choice = get_user_choice(name)
        ai_choice = get_ai_choice()
        result = find_winner(user_choice, ai_choice, name)
        print(f'{name} choice is: {choice_meaning[user_choice]}')
        print(f'AI choice is: {choice_meaning[ai_choice]}')
        print(result)
