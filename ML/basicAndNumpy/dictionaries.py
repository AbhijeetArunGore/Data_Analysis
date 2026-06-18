#unordered,mutable,not allow dulpicates
#key value pair
abi={"a":1,"b":2,"c":3}
print((abi))
#modify values
abi["b"]=4
print(abi)
#default values
abi.get("e",9)
print(abi)
#add values
abi["d"]=4
print(abi)
#pop
abi.popitem()
print(abi)
#for loop
for key in abi:
    print(key,abi[key])
for key , value in abi.items():
    print(key,value)
for value in abi.values():   #instead of values write keys 
    print("values :",value)
#modify values
print(abi.get("e"))
# for length use len function 
# for concatenation use str
#for type use type function