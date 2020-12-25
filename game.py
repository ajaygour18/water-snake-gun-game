import random
list1=["water","snake","gun"]

c=random.choice(list1)
county=0
countc=0
chance=9
while(chance>=0):
    your_choice=input("enter your choice:")
    if your_choice=="water":
        if c=="water":
            print("c is also",c," game tie")
            chance-=1
            continue
            
        elif c=="snake":
            print("c is",c,"you lose")
            countc+=1
            chance-=1
        elif c=="gun":
            print("c is",c,"you win")
            county+=1
            chance-=1
    if your_choice=="snake":
        if c=="water":
            print("c is",c,"you won")
            county+=1
            chance-=1
        elif c=="snake":
            print("c is also",c,"tie")
            chance-=1
            continue
        elif c=="gun":
            print("c is",c,"you lose")
            countc+=1
            chance-=1
    if your_choice=="gun":
        if c=="water":
            print("c is",c,"you lose")
            countc+=1
            chance-=1
        elif c=="snake":
            print("c is",c,"you won")
            county+=1
            chance-=1
        elif c=="gun":
            print("c is also",c,"tie")
            chance-=1
            continue
    if chance==0:
        print("game over")
        break
if countc>county:
        print("computer won")
elif county>countc:
        print("you won")