
import random
guess_num = int(input("guess a number"))
random_num = random.randint(1,100)
guess = 1
game_over = False

while not game_over:
    if guess_num == random_num:
        print("YOU WIN !!!and you guess this number in {guess} times")
    game_over = True

    else:
        if guess_num > random_num:
            print("too high")
    
        else:
            print("too low") 

        guess += 1
        guess_num = int(input("guess the number again"))
        


           
