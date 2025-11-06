D={"nagashree":'4/11/2005',
   "vasukeshava":'22/5/2010',
   "hema desai":'19/8/1976',
   "murarji desai":'13/3/1973'}
print(D)
#accessing
print(D["hema desai"]) #19/8/1976
print(D.get("murarji desai")) #13/3/1973
#assignation
D["SUDEEP"]='2/9/1975'
print(D) #{'nagashree': '4/11/2005', 'vasukeshava': '22/5/2010', 'hema desai': '19/8/1976', 'murarji desai': '13/3/1973', 'SUDEEP': '2/9/1975'}  
#operations:- clear,copy,pop,del
#D.pop("SUDEEP")
del D["SUDEEP"]
print(D) #{'nagashree': '4/11/2005', 'vasukeshava': '22/5/2010', 'hema desai': '19/8/1976', 'murarji desai': '13/3/1973'}

print(D.keys()) #dict_keys(['nagashree', 'vasukeshava', 'hema desai', 'murarji desai'])
print(D.values())#dict_values(['4/11/2005', '22/5/2010', '19/8/1976', '13/3/1973'])
print(D.items())#dict_items([('nagashree', '4/11/2005'), ('vasukeshava', '22/5/2010'), ('hema desai', '19/8/1976'), ('murarji desai', '13/3/1973')])
#itrms operation gives us output as tuple in inside list which is insie of dictionary.
relation={'daughter':'19','son':'15','mom':'49','dad':'52'}
D.update(relation)
print(D)#{'nagashree': '4/11/2005', 'vasukeshava': '22/5/2010', 'hema desai': '19/8/1976', 'murarji desai': '13/3/1973', 'daughter': '19', 'son': '15', 'mom': '49', 'dad': '52'}

#lists of dicts

STORE1={
    "name":"rice","weight":"3kg","price":int(502)
}    

STORE2={
    "name":"basmathi","weight":"6kg","price":int(1002)

}

print(f"(total price:-{STORE1["price"]+STORE2["price"]}")