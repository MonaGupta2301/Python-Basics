# GAME FOR SCISSOR,PAPER AND ROCK
import random
def game(human,com):
    if(com=='s'):
        if(human=='p'):
            print(" * * * *  Computer Winner * * * *")
            print(" * * * *  You Lose * * * *")
        elif(human=='r'):
            print(" * * * *  You Winner * * * *")
            print(" * * * *  Computer Lose * * * *")
    if(com=='p'):
        if(human=='s'):
            print(" * * * *  You Winner * * * *")
            print(" * * * *  Computer Lose * * * *")
        elif(human=='r'):
            print(" * * * *  Computer Winner * * * *")
            print(" * * * *  You Lose * * * *")
    if(com=='r'):
        if(human=='p'):
            print(" * * * *  You Winner * * * *")
            print(" * * * *  Computer Lose * * * *")
        elif(human=='s'):
            print(" * * * *  Computer Winner * * * *")
            print(" * * * *  you Lose * * * *")
    if( com==human):
        print("\n Both Are Same These Time ")
        print("\n * * * * * ITS DRAW * * * * *")
        print("\n Try Again")


print("\n ***********Game********")
print("\n SCISSOR , PAPER & ROCK ")
print("\n You Have Three Choices :")
print("\n Press s For SCISSOR : ")
print("\n Press p For PAPER : ")
print("\n Press r For ROCK : ")
print("\n Computer Chooses ")
human = input("\n Enter Your Choice :")
ran = random.randint(1,3)
if(ran==1):
    ran = 's'
elif(ran==2):
    ran = 'p'
elif(ran==3):
    ran = 'r'
game(human,ran)

print(f"\n Computer Choose : {ran} ")
print(f"\n You Choose : {human} ")