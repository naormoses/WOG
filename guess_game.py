import random

def generate_number(difficulty):
    seceret_number = random.randrange(1,difficulty+1)
    return seceret_number


def get_guess_from_user(difficulty):
    user_guess = int(input(f'Please Input a number within the range of 0 to {difficulty}: '))
    
    while user_guess < 0 or user_guess > difficulty:
        user_guess = int(input('Invalid input! Please enter a number corresponding to the range mentioned above:'))
    
    return user_guess


def compare_results(seceret_number, user_guess):
    is_equal = (seceret_number == user_guess)
    return is_equal


def play(difficulty):
    seceret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if compare_results(seceret_number, user_guess):
        print('Well guessed!')
        return True
    else:
        print('Not quite!')
        return False
    
    

# if __name__ == '__main__':
#     play()