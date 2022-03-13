import random

print("Let's play a game! ")

user_choice = ''

while (user_choice != 'scissors' and 
        user_choice != 'paper' and 
        user_choice != 'rock'):
        user_choice = input("You need to choose scissors, paper or rock and enter it >> ")

#choices = list("scissors", "paper", "rock")
# print(choices)

def com_choice(choice):
    if choice == 0:
        comp_ch = 'scissors'
    elif choice == 1:
        comp_ch = 'paper'
    else:
        comp_ch = 'rock'
    return comp_ch

computer_choice = com_choice(random.randint(0,2))

def check_result(player, computer):
    if user_choice == computer_choice:
        print("Draw")
    elif ((user_choice == 'scissors' and computer_choice == 'paper')
    or (user_choice == 'rock' and computer_choice == 'scissors')
    or (user_choice == 'paper' and computer_choice == 'rock')):
        print('Player wins')
    else:
        print('Computer wins')
check_result(user_choice, computer_choice)
print('Payer chose: ', user_choice)
print('Computer chose:', computer_choice)