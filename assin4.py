#Question 1

tuple=("python",4.8,5,False)
print(tuple)
print(len(tuple))


#Question 2

tuple1=(2,4,5,7,8,2,1,45,34,76)
tuple2=("chandan","akshay","rithvik")
print("Largest value of tuple")
print(max(tuple1))
print("smallest value of tuple1")
print(min(tuple1))
print("smallest value of tuple2")
print(min(tuple2))


#Question 3

tuple=(21,40,67,78,84,68)
x=1
print(tuple)
for i in tuple:
    x=x*i
print(x)


#SETS
#Question1

seta={input("enter a set")for i in range(4)}
print(seta)
setb={input("enter a set")for i in range(3)}
print(setb)
#intersection
setc = seta & setb
print(setc)
#difference
setd = seta - setc
print(setd)
#compare
sete = seta<=setb
print(sete)

#Dictionary
#Question 1


dict = {}
for i in range(10):
    name = input("enter name")
    marks = int(input("enter marks"))
    dict[name]= marks
print(dict)
            
#question 2

dict1 = sorted(dict.items(), key=lambda x:x[1])
print(dict1)



#Question 3


dict = {}
str = "MISSISSIPPI"
m = str.count('M')
i = str.count('I')
s = str.count('S')
p = str.count('P')

dict['M'] = m
dict['I'] = i
dict['S'] = s
dict['P'] = p
print(dict)
