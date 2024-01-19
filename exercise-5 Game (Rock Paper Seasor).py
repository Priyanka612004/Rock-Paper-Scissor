  #SNAKE WATER GUN GAME / ROCK PAPER SEASOR
import random
#co=user input and user=random no. of computer
def game():
    if (co==0):
        if(user==0):
            print('draw')
        elif(user==1):
            print('loose')
        elif(user==2):
            print('win')

    elif (co==1):
        if(user==0):
            print('win')
        elif(user==1):
            print('draw')
        elif(user==2):
            print('loose')

    elif (co==2):
        if(user==0):
            print('loose')
        elif(user==1):
            print('win')
        elif(user==2):
            print('draw')

user=random.randint(0,2)
print('0.rock 1.paper 2.seaser')
co=int(input('enter your choise: '))
print("You: ",co)
print("computer:" ,user)
game()