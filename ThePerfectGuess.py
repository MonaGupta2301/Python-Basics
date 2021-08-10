# The Perfect guess 
import random 
ran=random.randint(1,100)
print(ran)

print(" * * * * * * * The Perfect Guess * * * * * * * *  ")
print("\n You Have To Guess the Number Between 1 to 100")
user=0
guess=0
while(user != ran):
    print("\n  * * * * * * * * * * * * * * * * * * * * * * * ")
    user=int(input(" Enter Your Guess : "))
    print("\n  * * * * * * * * * * * * * * * * * * * * * * * ")
    guess=guess+1
    try:
        if(user<ran):
           print("\n Hint : Print the Grater Number Then You Typed ")
        elif(user==ran):
           pass
        else:
           print("\n Hint : Print the smaller Number Then You Typed ")
        if(user==ran):
           print("\n You Gesses It Right ")
           print(f"\n You Guess it in {guess} Guesses")
           print(f"\n Your SCORE is : {guess}")
    except Exception as e:
        print(f"\n\n You Entered Incorrect Value Plse Enter The Integer Type Value {e}")
                       