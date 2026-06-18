f=1,2,3,4,5  #tuple
print(f,'\n',type(f))
if 3 in f:
    print("present")
else:
    print("not present")
print(f[3])

print(f[1:6:2])  #start:end:jump

val=(10,20,30,40,50,60,70,80,90)
print(val[2:8:2])
print(val)
temp=list(val)
print(temp)
temp.extend([100,110])
print(temp)
val=tuple(temp)
print(val)

info=("abhijeet",22,"sppu","python")
(name,age,university,skill)=info
print("name is ",name)
print("age is ",age)
