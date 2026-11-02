import random,sys
guess = ''
win=0
looses=0
streak=0
best_win_streak=0
losing_streak=0
worst_losing_streak=0
while True:
    print('Guess the coin toss! Enter h or t:')
    print(f"{win} wins,{looses} looses, \nYour win streak is {streak}, \nYour best streak is {best_win_streak}, \nYour losing streak is {losing_streak},\nYour worst losing streak is {worst_losing_streak}")
    
    guess = input()

    if guess=='q':
        print('quit')
        sys.exit()
    if guess not in("h",'t'):
        print("Not a valid input, Please enter either h or t")
        continue
    toss = random.randint(0,1) # 0 is t, 1 is h
    if toss ==1:
        toss ='h'
    else:
        toss = 't'
    
    if toss == guess:
        print('You got it!')
        win+=1
        streak+=1
        losing_streak=0
        if streak>best_win_streak:
            best_win_streak=streak
    else:
        print('Try Again',end=' ')
        looses+=1
        losing_streak+=1
        streak=0
        if losing_streak>worst_losing_streak:
            worst_losing_streak=losing_streak


