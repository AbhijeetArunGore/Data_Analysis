a=60
print(a)
del a
try:
    print(a)
except NameError:
    print("Variable 'a' is not defined")


if(0.1+0.2==0.3):
    print("true")
else:
    print("false")