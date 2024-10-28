import os
import random

def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        random_number = random.randint(1, 100)
        sequence.append(random_number)
    print(sequence)
    os.system('sleep 0.7')
    os.system('clear')
    return sequence

def get_list_from_user(difficulty):
    user_sequence = []
    for i in range(difficulty):
        user_number = int(input(f'Please enter a number between 1 and 100 for the {i + 1} number: '))
        user_sequence.append(user_number)
    return user_sequence

def is_equal(user_sequence, sequence):
    if user_sequence == sequence:
        return True
    return False

def play(difficulty):
    sequence = generate_sequence(difficulty)
    user_sequence = get_list_from_user(difficulty)
    if is_equal(user_sequence, sequence):
        print('Well guessed!')
        return True
    else:
        print('Not quite!')
        print(f'The correct sequence was: {sequence}')
        return False

# if __name__ == '__main__':
#     play()