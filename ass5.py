#Question 1

year=int(input("enter a year"))
if(year%4)==0:
    print("it is a lear year")
else:
    print("not a leap year")



#Question 2
    
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
if(length==breadth):
    print("it is a sqare")
else:
    print("it is a rectangle")


#Question 3


age1=int(input("enter the age1"))
age2=int(input("enter the age2"))
age3=int(input("enter the age3"))
if(age1>=age2 and age1>=age3):
    print("first is old")
elif(age2>=age1 and age2>=age3):
    print("second is old")
elif(age3>=age1 and age3>=age2):
    print("third is old")
else:
    print("all are of same age")


#Question 4

print("enter points")
points = int(input("enter the point"))
if(points>0 and points<=50):
    print("No Prize")
elif(points>=51 and points<=150):
    print("Congratulations!You won a Wooden Dog")
elif(points>=151 and points<=180):
    print("Congratulations!You won a Book")
elif(points>=181 and points<=200):
    print("Congratulatons!You won Chocolates")
else:
    print("sorry!No prize this time.")
    


#Question 5


quantity = int(input("enter quantity of items"))
cost = quantity * 10
if(cost > 1000):
    print("10% discount")
    discount = (cost*10)/100
    update = cost - discount
    print("you need to pay" ,(update))
else:
    print("you need to pay" ,(cost))
