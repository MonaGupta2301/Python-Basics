# Wap A Program In Which You Have A Game Function And which returns an integer value as A Score of Game
# now you also have an highscore.txt file which con tains a highscore which scored by a any preson so if
# you are plaing a game andscored higher that that person than change the score of highscore.txt file 
# mean you have to update it.
def game():
     return 4

s=game()
    with open("highscore.txt") as f:
        h=int(f.read())
    if(h>s):
        with open('highscore.txt','w') as w:
            w.write(str(h))
    else:
            w.write(str(s))
                 