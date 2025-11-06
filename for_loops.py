#lists using for loops
l=[1,24,47,452,224,455]

total=0
for num in l:
    print(total)    
    total=total+num
print(total)    

#doubling the no in list
dl=[]
for num in l:
    dl.append(num*2)
    print(dl)

#for loop for dictionaries
# over keys.values,and both
std_marks={"anad":85,"teja":89,"vijay":98}

for name in std_marks:
    print(name)
for marks in std_marks.values():
    print(marks)    
for name,marks in std_marks.items() :
    print(f"{name}--{marks}")   

#list comphrension
num=[1,2,3,4,5,6]
sq=[ n ** 2 for n in num]
print(sq)

n=[nm  for nm in range(1,11)]
edl=[nm**2 for nm in n if nm%2==0]
print(edl)

l=["chandu","ryan","devi","nagu"]
cl=[x[2] for x in l ]
print(cl)

#dictionary comphrension
names=["anand","geetha","seetha"]
d={namee:len(name) for namee in names}
print(d)

stdmarks={"devi":85,"manju":56,"hardsk":88,"nabfy":23}
distinction={key:value  for key,value in stdmarks.items() if value>85}
print(distinction)

#splitting strings

l=[int(num) for num in input("enter the list of elements:").split()]
print(l)