#[1,2,3,4]
list1=list()
mylist=[1,"s",2.2,'eee3']
list3=[1,6,4,3,5]
print(mylist[2:])
print(mylist)
print(mylist*2)
print(list1)
print(len(mylist))
print(list3[::-1])
hh=['a','b','c','d']
hh[1]='e'
print(hh)
hh.append('b')
print(hh)
hh.extend(['e','f'])
print(hh)
hh.insert(0,'z')
print(hh)
hh.pop(0)
print(hh)
hh.remove('e')
print(hh)
hh.insert(1,'b')
print(hh)
print(hh.count('a'))#counts number of times element occureed
print(hh.index('b'))
hhj=list()
hhj=hh.reverse()
print(type(hh),(hhj))
print(hh)
print(hhj)
list3=sorted(list3)
print(list3)
list3=sorted(list3,reverse=True)
print(list3)
print(min(list3),max(list3))

list4=list3.copy()
print(list4)
print(id(list3))
print(id(list4))

list3.clear()
print(list3)

naka=[1,2,3]
kana=[4,5,6]
nana=kana+naka
print("kana",kana)
print("naka",naka)
print("nana (kana+naka) :",nana)

#special

squares=[x**2 for x in range(10)]
print("squares :",squares)

even_square=[c**2 for c in range(10) if c%2==0]
# # print("even squares :",even_square)
# s={'a','b',1,(3,4)}
# print(type(s))