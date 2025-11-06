def marriage(boy,girl):
    print(f"Boy is {boy}")
    print(f"GIRL is {girl}")
    print(f"{boy} married {girl}")

marriage("chandan","shwetha")  #positional arguments
marriage(boy="ayush",girl="reena") #keyword arguments 


def tables(num=50):
    for i in range(1,11):
        print(f"{num}X{i}={num*i}")

tables()  #default arguments

def sum(a,b):
    return a+b     #return 
add=sum(5,6)
print(add)

def sum(*num):
    tot=0
    for i in num:
        tot+=1
        return tot
    sum(1,2,3,4)# variable positional arguments

def info(**details):
    for key,value in details.items():
        print(f" {key} :  {value}")

info(name="vade",support="saru",main="idli")     #variable keyword arguments

add= lambda a,b :a+b
print(add(1,3))

students=[
    {"name":"chandan","marks":89},
    {"name":"reetha","marks":94},
    {"name":"laila","marks":92}
]
students.sort(key=lambda x:x["marks"],reverse=True)
print(students)

def factioral(n):
    if n==0:
        return 1
    else:
        return n*factioral(n-1)  #recurssion
print(factioral(5))
#nested functions
def calculate(a,b):
    def add():
        print( a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():
        print(a/b)
    def floordiv():
        print (a//b)
    add()
    sub()
    mul()
    div()
    floordiv()
print(calculate(5,6))  
