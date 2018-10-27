import random
a=["rock","paper","scissor"]
n=5
sumu=0
sumc=0
print("lets play")
print("there are five chances")
for i in range(0,5):
    u=input("what you choose\n")
    c=random.choice(a)
    print(c)
    if(u==c):
        print("no body has points")
    elif(u=="rock" and c=="scissor"):
        sumu=sumu+1
    elif(u=="paper" and c=="rock"):
        sumu=sumu+1
    elif(u=="scissor" and c=="paper"):
        sumu=sumu+1
    elif(c=="rock" and u=="scissor"):
        sumc=sumc+1
    elif(c=="paper" and u=="rock"):
        sumc=sumc+1
    elif(c=="scissor" and u=="paper"):
        sumc=sumc+1
if(sumu>sumc):
    print("user had won")
elif(sumc>sumu):
    print("i had won")
