# snake water gun game
import random
print("hey user!welcome to SNAKE,WATER,GUN game")
list=["snake","water","gun"]
user_count=0
comp_count=0
i=0
while(i<10):
    rand = random.choice(list)
    choice = input("enter your choice b/w snake,water and gun\n")
    if rand == choice:
        print("draw")
    elif rand == "snake" and choice == "gun":
        user_count = user_count + 1
        print(f"my choice was {rand}.")
        print("you won")
        i = i + 1
    elif choice == "snake" and rand == "gun":
        comp_count = comp_count + 1
        print(f"my choice was {rand}.")
        print("I won")
        i = i + 1
    elif rand == "water" and choice == "snake":
        user_count = user_count + 1
        print(f"my choice was {rand}.")
        print("you won")
        i = i + 1
    elif choice == "snake" and rand == "water":
        comp_count = comp_count + 1
        print(f"my choice was {rand}.")
        print("I won")
        i = i + 1
    elif rand == "gun" and choice == "water":
        user_count = user_count + 1
        print(f"my choice was {rand}.")
        print("you won")
        i = i + 1
    elif choice == "gun" and rand == "water":
        comp_count = comp_count + 1
        print(f"my choice was {rand}.")
        print("I won")
        i = i + 1
    else:
        print("you entered wrong input!try again!")
print("THE RESULT IS :- ")
diff1=comp_count-user_count
diff2=user_count-comp_count
if comp_count>user_count:
    print(f"i won by {diff1}.")
elif comp_count<user_count:
    print(f"you won by {diff2}.")
elif comp_count==user_count:
    print("it's a draw match")