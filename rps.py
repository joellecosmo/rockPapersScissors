import random
weapons = ['R', 'P', 'S']
weapons_dict={
    'R':'🪨',
    'P':'📄',
    'S': '✂️',
    }
def process_game(user_weapon, computer_weapon):
    print(f"Your weapon is {weapons_dict[user_weapon]} vs Computer weapon is {weapons_dict[computer_weapon]}")
    if user_weapon == computer_weapon:
        return 0
    if user_weapon == 'R':
        if computer_weapon == 'S':
            return 1
        else:
            return -1
    if user_weapon == 'S':
        if computer_weapon == 'P':
            return 1
        else:
            return -1
    if user_weapon == 'P':
        if computer_weapon == 'R':
            return 1
        else:
            return -1
sets = int(input('Enter number of sets'))
wins, losses, ties = 0 , 0 , 0
for i in range(1, sets+1):
    while True:
            user_weapon = input("Enter your weapon: \n R is for rock \n P is for paper \n S is for scissors \n").upper()
            if user_weapon not in weapons:
                print("Invalid weapon, please try again")
            else:
                break
    computer_weapon= random.choice(weapons)
    result = process_game(user_weapon, computer_weapon)
    if result == 1:
        wins=wins+1
        print("YOU WIN!")
    elif result == -1:
        losses=losses+1
        print("YOU LOSE!")
    else:
        ties=ties+1
        print("Tie...")

print('-'*10)
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Ties: {ties}")
print('-'*10)

