'we can use both comparision and logical operators for if stsmts'
#if - else
x= 5

if x%2==0 :
    print("IT OS EVEN NUMBER")
else :
    print("IT IS ODD NUMBER")  

#if ellif else

num=2

if num>0 :
    print("it is positive")
elif num<0 :
    print("it is negative")    
else :
    print("it is zero") 


age=2

if age < 5:
    print("Bus pass is free")
elif age>60 and age==60:
    print("passenger gets senior citizen pass") 
else:
    print("Bus pass is full fare")  

time="12 PM" 

match time :
    case "8 AM":
        print("It is Breakfast time")
    case "1 PM" :
        print("It is Lunch time")   
    case "8 PM" :
        print("It is Dinner time")
    case _ :
        print("It is not a meal time") 

print("Welcome to library membership ")
check_age=int(input(("Enter the age:"))) 
if check_age<18 :
    print("Student library membership approved")
elif check_age>60 :
    print("Senior citizen membership approved")
else :
    print("Regular membership approved")

    #LOOPS
i=0    
while i <=10:
    print(i)                         
    i=i+1

#factorial

num = 5
factorial = 1
while num > 0:
  print( factorial) 
  factorial *= num

  num -= 1
 
 # for loop

#in sequence
cities=["bangluru","mysuru","chitradurga","davangere"]

for city in cities:
    print(city)

#range
for i in range(1,20,3):
    print(i,end=" ")  

#looping over strings
name='nagashree'

for letter in name:
    print(letter*4)
#using emureate
hesaru="vasu"
for index,letter in enumerate(hesaru):
    print(letter*(index+1)) 

# for loop for lists
d={"name":"vasu","age":15,"class":"10th"}

for key,value in d.items():
    print(key," ",value)

#nested loops
for i in range(1,11):
    print(f" 2x{i}={2*i}")

for i in range(2,11):
    for j in range(1,11):
        print(i,"X","=",j)    








