language=("java","c","c++","python")
backend=("SQL",)
#accesing
print(backend) #output=('SQL',)
print(language[2]) #output=c++
#slicing
print(language[1:3]) #output=('c', 'c++')

# one can't add a element to tuple
#concatenation
tuple_1=('a','b','c',)
tuple_2=('A','B','C',)
tuple_com= tuple_1 + tuple_2
print(tuple_com) #output=('a', 'b', 'c', 'A', 'B', 'C')

#repeation
repeat=('a','b')*5

print(repeat) #output=('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
#membership operators
city=('CTA','DVG','HLR','TUM',)
print("CTA" in city) #output=True

#methods
#count--- number of times the elemnt is repeated
num=(1,2,3,5,2,1,3,6,1,56,1,5,23)
print(num.count(1)) #output=4

#index
print(num.index(56))  #output=9

#SETS:- IT IS UNORDERD,UNINDEXED AND DUPLICATE ITEMS ARE NOT ALLOWED
s={50,24,100,1}
print(s)  #output={24, 1, 50, 100}

#union,imtersection,difference
s1={1,2,3}
s2={3,4,5}
print(s1 | s2) #output={1, 2, 3, 4, 5}
print(s1 & s2 ) #output={3}
print(s1 - s2) #output={1, 2}
#operations:-  add,remove,discard,clear,pop



