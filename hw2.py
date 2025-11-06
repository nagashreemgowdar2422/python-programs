#swap nos without third variable
x =input("enter the 1st numbers:")
y=input("enter the 2nd numbers:")
x,y=y,x
print(f"X={x} and Y={y}..After swap")
#string manipulation using + 
name=input("Enter your name:")
age=(input("Enter your age:"))

print("hello!" +  name  +  "you are"  +  (age))

#USING f strings
print(f"hello {name}! you are {age} old")

sample=input("Enter the sentence :- ")
print(sample.upper())
print(sample.lower())
print(sample.strip())
print(sample.replace(" ","_"))
res= sample.replace("  ","")
print(res)
greet=input("sentence:")
print("length of given string:- ",len(greet.replace(" ","")))


print("Hello\n\tworld!", "\n This is a blacklash '\'")