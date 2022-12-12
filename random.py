import random
def shoot(me):
    print("0 is for rock, 1 is for paper, 2 is for scissor")
    
    if me==0:
        computer=random.randint(0,2)
        if computer==0:
            print("you and computer chose rock, its a draw")
        elif computer==1:
            print("you chose rock,computer chose paper. paper covered your rock, you lose")
        else:
            print("you chose rock, computer chose scissor. rock hit scissor, you win")
    elif me==1:
        computer=random.randint(0,2)
        if computer==0:
            print("you chose paper,computer chose rock. paper covered your rock, you win")
        elif computer==1:
            print("you and computer chose paper. its a draw")
        else:
            print("you chose paper, computer chose scissor. scissor cut paper, you lose")
    elif me==2:
        computer=random.randint(0,2)
        if computer==0:
            print("you chose scissor,computer chose rock. rock hit scissor, you lose")
        elif computer==1:
            print("you chose scissor,computer chose paper. scissor cut paper, you win")
        else:
            print("you and computer chose scissor, its a draw")
    else:
        print("you didnt pick either 0,1,2")

shoot(1)