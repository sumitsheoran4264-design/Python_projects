import random
from art import logo, vs
from data import data
#higer lower
def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return(f"{account_name}, {account_descr}, from {account_country}.")


def is_guess_correct(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    
account_b = random.choice(data)

score = 0
game_on = True
print(logo)

while game_on:
    

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print("Account A:",format_data(account_a))

    print(vs)

    print("Against B:",format_data(account_b))

    choice = input("How has more follower? Type A or B: ").lower()
    print(logo)

    account_a_follower = account_a['follower_count']
    account_b_follower = account_b['follower_count']


    if (is_guess_correct(choice, account_a_follower, account_b_follower)):
        score += 1
        print(f"You are right, your current score is {score}")
    else:
        print(f"You guess wrong, your final score is: {score}")
        game_on = False
