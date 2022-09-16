import random


def game(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == "r":
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False

print("Computer's turn: Rock(r) Paper(p) Scissors(s)?")
randNo = random.randint(1,3)
if(randNo == 1):
    comp = 'r'
elif(randNo == 2):
    comp = 'p'
elif(randNo == 3):
    comp = 's'
you = input("Your turn: Rock(r) Paper(p) Scissors(s)?")

a = game(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("This Game is Tie!")
elif a == True:
    print("You Win!")
elif a == False:
    print("You Lose!")
