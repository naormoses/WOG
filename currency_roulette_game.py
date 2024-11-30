import random
import requests
# import PyCurrency_Converter

api_key = "82bd1879c317e22c06abfb72"

def get_convertion_rate():
    USD_to_ILS_rate = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD").json()["conversion_rates"]["ILS"]
    return USD_to_ILS_rate

def get_money_interval(difficulty):
    usd_amount = random.randrange(0,100)
    print(f'Your amount is {usd_amount} USD')
    interval_allowed = 10 - difficulty
    return usd_amount, interval_allowed


def get_guess_from_user() :
    user_guess = int(input('Please input yout guess for the currency in shekels: '))
    return user_guess


def compare_results(usd_amount, interval_allowed):
    USD_to_ILS_rate = get_convertion_rate()
    user_guess = get_guess_from_user()
    is_allowed = abs(user_guess - (usd_amount*USD_to_ILS_rate)) <= interval_allowed
    if is_allowed:
        return True
    else:
        return False


def play(difficulty):
    usd_amount, interval_allowed = get_money_interval(difficulty)
    if compare_results(usd_amount, interval_allowed):
        print('Well guessed!')
        return True
    else:
        print('Not quite!')
        return False


# if __name__ == '__main__':
#     difficulty = int(input('Please select the Difficulty between 1 and 5 you would like: '))
#     play(difficulty)