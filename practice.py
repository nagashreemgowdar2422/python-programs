print("nagashree"+" m "+"gowdar") # concatenation
First_name='Nagashree'
Middle_name='M'
Last_name='Gowdar'
Age="19"
#USING f- strings 
print(f"My name is {First_name} {Middle_name} {Last_name}. I am {Age}  years old.")
Greet="hello!"
print(Greet*3)
#USING string methods
test=input("enter the sample sentence:-")
print(test.upper())
print(test.lower())
print(test.strip())
print(test.replace("","_"))
RES=test.replace(" ","")
print(len(RES))

#accesing
string="NAGASHREE"
print(string[4:8])
print(string[:4])
print(string[4:])
#negative indexing
print(string[-3])
print(string[::2])
print("hello\n\tworld!.\nthis is the use of escape sequence '/'")


