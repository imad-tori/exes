import random


while True:

    play = input("do you want to play? y/n\n").lower()
    if play == "n":
        break
    rand_num = random.randint(1,20)
    tries = 0
    success = False

    while tries < 5:

        tries+=1
        user_num = int(input("guess the number: "))
        if rand_num > user_num:
            print("Too low!")
        elif rand_num < user_num:
            print("Too high!")
        else:
            print("Correct! You guessed it!")
            success = True
            break

    if not success:
        print(f"Game over! The correct number was {rand_num}")