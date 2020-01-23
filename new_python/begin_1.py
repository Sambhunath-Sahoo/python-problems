import random
winning_num = random.randint(1,5)
guess = 1
num = int(input("guess a number betn 1 to 100 :"))
game_over = False

while not game_over:
    if num == winning_num:
        print(f"YOU WIN !!!. and you guess this number in {guess} time")
        break
    else:
        if num > winning_num:
            print("too high")
            guess += 1
            num = int(input("guess again :"))
        else:
            print("too low")
            guess += 1
            num = int(input("guess again :"))


