import random

choices = ['r', 'p', 's']

choice_meaning = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors',
}

user_score = 0
ai_score = 0

counter = 0

while counter < 5:
    user_choice = input('select from Rock, Paper, Scissors: (r, p, s) ')

    ai_choice = random.choice(choices)

    if user_choice in choices:
        print(
            f'Your choice is {choice_meaning[user_choice]}.\
            Random choice is {choice_meaning[ai_choice]}.'.replace('    ', ' ')
        )
        # r > s - p > r - s > p
        if user_choice == ai_choice:
            print('Tie')
        elif user_choice == 'r' and ai_choice == 's':
            print('user+1!')
            user_score += 1
        elif user_choice == 'p' and ai_choice == 'r':
            print('user+1!')
            user_score += 1
        elif user_choice == 's' and ai_choice == 'p':
            print('user+1!')
            user_score += 1
        else:
            print('AI+1!')
            ai_score += 1
    else:
        print('Invalid input')
        counter -= 1

    print(f'User score: {user_score} | AI score: {ai_score}')

    print('\n', '-' * 15, '\n')

    counter += 1

if user_score > ai_score:
    print(f'User won with score: {user_score}')
elif user_score < ai_score:
    print(f'AI won with score: {ai_score}')
else:
    print(f'It\'s a tie. score: {user_score}')
