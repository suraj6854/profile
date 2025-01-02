import random
l=['Rock','Paper','Scissor']
while True:
    ccount=0
    ucount=0
    uc=int(input('''
    rock paper scissor Game Start:
    1: Yes 
    2:No Exit    
    '''))
    if uc==1:
        for a in range(1,4):
            userinput=int(input('''
        1 Rock
        2 Paper
        3 Scissor
        '''))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="Paper"
            elif userinput==3:
                uchoice="Scissor"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("Your value", uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=='Rock' and Cchoice=='Scissor')or(uchoice=='Paper' and Cchoice=='Rock')or(uchoice=='Scissor' and Cchoice=='Paper'):
                print("Computer value",Cchoice)
                print("user value",uchoice)
                print("You win")
                ucount=ucount+1
            else:
                print("Computer value", Cchoice)
                print("user value", uchoice)
                print("Computer Win")
                ccount = ccount + 1
        if ucount==ccount:
            print("Final Game Draw")
            print("user score",ucount)
            print("computer score",ccount)
        if ucount > ccount:
            print("Final You win")
            print("user score", ucount)
            print("computer score", ccount)
        else:
            print("Final computer win")
            print("user score", ucount)
            print("computer score", ccount)
    else:
        break