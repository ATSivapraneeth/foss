print("welcome to shopping mall")
print("the items in shop")
print("The sports items are:")
print("    foot ball= Rs.400/-")
print("    badmention=Rs.250/-")
print("    volley ball=Rs.550/-")
print("The food items in our mall are:")
print("    hydensic biscuits =Rs.20/-")
print("    cup noodles= Rs.40/-")
print("    choclate cake= Rs.60/-")
print("Mobiles in our mall are :")
print("    iphone X = Rs.100,000/-")
print("    iphone 8 =Rs.70,000/-")
print("    iphone 7s =Rs.40,000/-")
cart=[]
noofq=[]
import random
c=["A23bZ","hJ2B32","z2MN12","45CVnb2","DF23Jhh","Fgg23G"]
capctha=random.choice(c)
product=["foot ball","badmention","volley ball","hydensic biscuits","cup noodles","choclate cake","iphone X","iphone 8","iphone 7s"]
price=[400,250,550,20,40,60,100000,70000,40000]
total=0
while(True):
    a=input("select the item you want ")
    n=cart.append(a)
    b=product.index(a)
    cost=price[b]
    quantity=int(input("no of quanties you required "))
    nfq=noofq.append(quantity)
    tcost=quantity*cost
    total=total+tcost
    print("do you want to continue(y,n)")
    ch=input()
    if(ch=="n"):
        break

coupon=input("do you have coupons ")
print("no of items you have choosen",cart)
print("no of respected quantites of above choosen items",noofq)
if(coupon=="yes"):
    print(capctha)
    d=input("write a capctha ")
    if(d==capctha):
        print("capcth is correct and you will get offer")
        print("The total price is: RS.",total)
        print("you have a discount of 4%")
        discount=(4/100)*total
        totalprice=total-discount
        print("Total price after discount is Rs.",totalprice)
    else:
        print("wrong capctha")
        print("the total price is Rs.",total)
else:
    print("the total price is Rs.",total)
print("how would you like to pau")
print("cash or card")
payment=input()
if(payment=="card"):
	print("enter the pin")
	input()
	print("payment successfull")
else:
	print("ok sir please give cash")
print("thank you for shopping")
print("please give the feedback")
feedback=["excellent","super","good","bad"]
print(feedback)
f=input()
for i in range(0,3):
    if(f==feedback[i]):
        print("thank u for giveing feedback")
        print("please come again")








    
