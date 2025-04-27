# rules:

# winner : losers

# 2 Cross : 4 Uppercut 3 Hook 

# 1 Jab : 2 Cross

# 4 Uppercut : 1 Jab 

# 3 Hook : 1 Jab 4 Uppercut

import random

rounds_number = int(input("1: regular fight\n2: championship\nchoose number: ")) * 3
u_score=0
comp_score=0

for i in range(rounds_number):

    user_num = int(input("1: Jab\n2: Cross\n3: Hook\n4: Uppercut\nenter number: "))
    comp_num = random.randint(1,4)

    if (user_num == 4 or user_num == 3) and comp_num == 1:
        u_score+=1

    elif (user_num == 2 or user_num == 3) and comp_num == 4:
        u_score+=1

    elif user_num == 2 and comp_num == 3:
        u_score+=1

    elif user_num == 1 and comp_num == 2:
        u_score+=1

    else:
        comp_score+=1

if u_score > comp_score:
    print("you win!")
elif u_score < comp_score:
    print("you lose!")
else:
    print("tied!")