#Question 1


a = [(int(input("enter the values")))for i in range(10)]
print(a)


#question 2


while True:
    print("welcome")


#Question 3


l1 = []
for x in range (5):
    y = int(input("enter the values"))
    l1.append(y)
print(l1)
l2=[]
for x in l1:
    z=x*x
    l2.append(z)
print(l2)


#Question 4

l1=[2,4,'banana',6,9,'kiwi',7,4]
print(l1)
l2=[]
l3=[]
l4=[]
for x in l1:
    if type(x) == int:
        l2.append(x)
    elif type(x) == str:
        l3.append(x)
    elif type(x) == float:
        l4.append(x)
print("list of intergers",l2)
print("list of strings",l3)
print("list of float",l4)


#question 5

even=[]
odd=[]
for x in range(1,101):
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("list of even",even)
print("list of odd",odd)



#Question 6

print ("Pattern ")
for i in range(0, 5):
    for j in range(0, i+1):
        print("* ",end="")
    print()


#Question 7


d = {}
for i in range(5):
    name = input("enter name")
    age = int(input("enter age"))
    d[name]=age
    print(d)


#Question 8

l1 = []
for x in range(5):
    s = input("enter elements")
    l1.append(s)
    print(l1)

d = input("enter elements to be deleted")
for x in l1:
    if x==d:
        l1.remove(x)
else:
    print("elements not present")
print("the list is",l1)
