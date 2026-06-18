#------------------------1---------------------
string1="hello world"
print(string1)
print(type(string1))
num=3
num1=4
num2=4.0
print(type(num))
print(type(num2))
val=True
print(type(val))
print("string1 - ",string1)
print("num-",num)
print("num2-",num2)
print("val-",val)
print(num,num2)
print(type(num),type(num2))
add=num+num1
print(add)
print("sub",num-num1)
print("multiplication",num*num1)
print("division-",num/num1)
print("floor division-",num//num1)
print("remender",num%num1)
print(type(num/num1))
new=1.0
new1=2.6
print("float add",new+new1)
print("float sub",new-new1)
print("int+float",num+new)
#inpput
string2=input("enter your sentence:")
print("yuor sentence is -",string2,"and type is ",type(string2))
print(string2.upper())
print(string2.lower())
print(string2.title())
print("the number of a in your string",string2.count('a'))
print(string2.replace('a',"A"))
print("the string lenght is ",len(string2))
print("location of a i your string",string2.find('a'))

#--------------------------2---------------------------
print(5 * 4 + 1)
print(1 + 5 * 4)
print(5 * (4 + 1) )
print(2==2)
print(True and False)
print(False & False)
print(not True)
print(not False)
print(abs(-2))
print(abs(-2.1))
print(round(3.45))
print(round(-3.95))
print(round(3.46, 1))
print(round(3.46, 2))
num1 = 'Hello Abhi'
num2 = '5'
print(num1 + num2)

x = 7
if x > 10:
    print('x is greater than 10')
    if x > 20:
        print('x is greater than 20')
        if x > 30:
            print('x is greater than 30')
        else:
            print('x is smaller than 30')
    else:
        print('x is smaller than 20')
else:
    print('x is smaller than 10')


#--------------------------3---------------------------

a = [1, 2, 3]
b = a
b.append(4)
print(a)      # [1, 2, 3, 4]  (same object)

# Proper copy
c = a.copy()
c.append(5)
print(a, c)
import copy

x = [[1, 2], [3, 4]]
y = x.copy()
z = copy.deepcopy(x)

y[0].append(99)
print(x)   # changed
print(z)   # unchanged
nums = [1, 2, 3, 4, 5, 6]

squares = [n*n for n in nums]
evens = [n for n in nums if n % 2 == 0]
conditional = [n if n % 2 == 0 else -n for n in nums]

print(squares, evens, conditional)
cubes = [i**3 for i in range(5)]
print(cubes)

data = [(1, 3), (4, 1), (2, 2)]
data.sort(key=lambda x: x[1])
print(data)

names = ['Abhijeet', 'ram', 'Shyam']
names.sort(key=len)
print(names)
nums = [3, 1, 2]
x = nums.sort()
print(x)        # None
print(nums)     # [1, 2, 3]

nums = [3, 1, 2]
y = sorted(nums)
print(nums, y)
lst = [10, 20, 30, 40]

lst.remove(20)   # by value
print(lst)

lst.pop(1)       # by index
print(lst)

del lst[0]       # delete without return
print(lst)
# list -> O(n)
# set  -> O(1)

nums = [1, 2, 3, 4, 5]
print(3 in nums)

a = [1, 2, 3]
b = ['a', 'b', 'c']

zipped = list(zip(a, b))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sub in nested for item in sub]
print(flat)
nums = [1, 2, 3, 4, 5]

# WRONG
for n in nums:
    if n % 2 == 0:
        nums.remove(n)

print(nums)  # unpredictable

# RIGHT
nums = [n for n in nums if n % 2 != 0]
print(nums)
items = ['a', 'b', 'a', 'c', 'b', 'a']
freq = {}

for i in items:
    freq[i] = freq.get(i, 0) + 1

print(freq)
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())
print(stack)
# pop(0) is O(n) -> bad
# deque is preferred (theory question)
from collections import deque

q = deque([1, 2, 3])
q.append(4)
print(q.popleft())
print(q)
print([[]] * 3)     # same reference
print([[] for _ in range(3)])  # different lists

#--------------------------4---------------------------

t = (1, 2, 3)
# t[0] = 100     # ❌ TypeError (immutable)
x = ([1, 2], [3, 4])
x[0].append(99)
print(x)        # tuple unchanged, list inside changed

a = (5)
b = (5,)

print(type(a))  # int
print(type(b))  # tuple

data = (10, 20, 30)
a, b, c = data
print(a, b, c)

x, *y, z = (1, 2, 3, 4, 5)
print(x, y, z)

a, b = 5, 10
a, b = b, a
print(a, b)

t = (1, 2, 3)
d = {t: "valid"}     # tuple can be dict key
print(d)

t = (1, 2, 3, 2, 2, 4)
print(t.count(2))
print(t.index(3))
t = (1, 2, 3, 4, 5)
print(3 in t)   # O(n)

t = (10, 20, 30, 40)
s = t[1:3]
print(s, type(s))


a = (1, 2)
b = (3, 4)

print(a + b)
print(a * 3)
t = ((1, 2), (3, 4), (5, 6))
print(t[1][0])   # 3
t = (3, 1, 2)
sorted_t = tuple(sorted(t))
print(sorted_t)
def calc(a, b):
    return a+b, a-b, a*b

res = calc(10, 5)
print(res)

x, y, z = calc(10, 5)
print(x, y, z)
t = ([0],) * 3
t[0].append(1)
print(t) 
a = {'x': 1}
b = a
b['y'] = 2
print(a)        # {'x': 1, 'y': 2}  (same reference)

c = a.copy()
c['z'] = 3
print(a, c)
import copy

d1 = {'a': [1, 2], 'b': 3}
d2 = d1.copy()
d3 = copy.deepcopy(d1)

d2['a'].append(99)
print(d1)   # changed
print(d3)   # unchanged

valid = {(1, 2): "ok"}
print(valid)

# invalid:
# d = {[1,2]: "fail"}   # ❌ TypeError
data = {'a': 10}

print(data.get('a'))       # 10
print(data.get('b'))
# print(data['b'])

words = ['a', 'b', 'a', 'c', 'b', 'a']
freq = {}

for w in words:
    freq.setdefault(w, 0)
    freq[w] += 1

print(freq)

nums = [1, 2, 3, 4]
squares = {n: n*n for n in nums if n % 2 == 0}
print(squares)

d = {'a': 1}
d.update({'b': 2, 'a': 100})
print(d)   # a overwritten

d = {'a': 1, 'b': 2, 'c': 3}

print(d.pop('b'))   # removes specific key
print(d)

print(d.popitem())  # removes LAST inserted item (Python 3.7+)
print(d)

d = {'x': 1, 'y': 2}

# WRONG
# for k in d:
#     d[k+1] = 100   # ❌ RuntimeError

# RIGHT
for k in list(d.keys()):
    d[k] += 10

print(d)
scores = {'ram': 90, 'shyam': 85, 'mohan': 95}

sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1]))
print(sorted_by_value)
company = {
    'name': 'Apple',
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
}

print(company['founders']['first'])
#---------------------------5.DICTIONARY-------------------------
a = {'x': 1}
b = {'y': 2, 'x': 100}

merged = a | b
print(merged)
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, [])

d['a'].append(1)
print(d)    # same list shared

# correct
d = {k: [] for k in keys}
d['a'].append(1)
print(d)

items = [('fruit', 'apple'), ('fruit', 'mango'), ('veg', 'carrot')]
group = {}

for k, v in items:
    group.setdefault(k, []).append(v)

print(group)

#--------------------------6.set---------------------------

# Unique elements only
s = {1, 2, 3, 2}
print(s)         # {1, 2, 3}

# From list (duplicates removed automatically)
lst = [1, 2, 3, 3]
s2 = set(lst)
print(s2)

# Empty set
empty = set()     #{} creates dict, not set

# Only hashable (immutable) elements can be added
s = {1, 2, (3, 4)}
# s.add([5,6])    # TypeError, list not allowed

# FrozenSet: immutable set
fs = frozenset([1,2,3])
# fs.add(4)       #AttributeError

s = {1, 2, 3}

s.add(4)          # add element
print(s)

s.remove(2)       # remove, KeyError if not found
# s.remove(5)     # ❌ KeyError

s.discard(5)      # safe removal, no error if not found

x = s.pop()       # removes arbitrary element
print(x, s)
s.clear()
print(s)
s = {1, 2, 3}
s2 = s.copy()
s2.add(4)
print(s, s2)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)           # union {1,2,3,4,5}
print(a & b)           # intersection {3}
print(a - b)           # difference {1,2}
print(a ^ b)           # symmetric difference {1,2,4,5}

# Methods version
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
a &= b    # intersection_update
print(a)

a |= b    # union_update
print(a)

a -= b    # difference_update
print(a)

a ^= b    # symmetric_difference_update
print(a)
x = {1, 2}
y = {1, 2, 3}

print(x.issubset(y))      # True
print(y.issuperset(x))    # True

print(x.isdisjoint(y))    # False
s = {1, 2, 3}
for i in s:
    print(i)#unordered
nums = [1, 2, 3, 4, 5, 6]

even_squares = {x*x for x in nums if x % 2 == 0}
print(even_squares)
s = "banana"
unique_chars = set(s)
print(unique_chars)    # {'b', 'n', 'a'}

# 2. Intersection of multiple sets
sets = [{1,2,3}, {2,3,4}, {3,4,5}]
result = set.intersection(*sets)
print(result)          # {3}

# 3. Union of multiple sets
result = set.union(*sets)
print(result)          # {1,2,3,4,5}

# 4. Empty set pitfalls
empty_dict = {}
print(type(empty_dict))    # dict, not set

empty_set = set()
print(type(empty_set))
fs1 = frozenset([1, 2])
fs2 = frozenset([2, 3])

# operations still possible
print(fs1 | fs2)           # union
print(fs1 & fs2)           # intersection

# cannot modify fs1
# fs1.add(4)  # ❌ AttributeError
lst = [1,2,2,3,4,4,5]
duplicates = {x for x in lst if lst.count(x) > 1}
print(duplicates)   # {2,4}

# better approach (O(n))
seen = set()
dupes = set()
for x in lst:
    if x in seen:
        dupes.add(x)
    else:
        seen.add(x)
print(dupes)
# 1. Order is NOT guaranteed
s = {5, 2, 3}
print(list(s))   # could be [2,3,5] or any order
# 2. Cannot index
# s[0]    # ❌ TypeError
# 3. Set elements must be hashable
# s.add([1,2])  # ❌ TypeError
#--------------------------7---------------------------
# ===============================
# FUNCTION BASICS
# ===============================

# Define & call
def hello():
    print("Hello World")
hello()

# Function type
print(type(hello))  # <class 'function'>

# Arguments
def greet(name):
    print(f"Hello {name}")

greet("Alice")
greet(123)          # works with any type

# Return values
def add(a, b):
    return a + b

print(add(5, 3))


# ===============================
# DEFAULT, KEYWORD, AND VARIABLE ARGUMENTS
# ===============================

# Default argument
def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Bob")

# Keyword arguments (order independent)
def distance(speed, time):
    return speed * time

print(distance(speed=10, time=3))
print(distance(time=3, speed=10))

# Variable positional arguments (*args)
def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5))  # 15

# Variable keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, val in kwargs.items():
        print(key, ":", val)

print_info(name="Alice", age=25)


# ===============================
# RETURN vs PRINT
# ===============================

def multiply(a, b):
    return a * b

result = multiply(5, 4)  # stores value
print(result)

# Printing inside function returns None
def multiply2(a, b):
    print(a * b)

x = multiply2(5, 4)
print(x)  # None


# ===============================
# SCOPE & LIFETIME
# ===============================

global_var = 100

def func_scope():
    local_var = 10
    print(local_var)       # accessible here
    print(global_var)      # accessible here

func_scope()
# print(local_var)         # ❌ Error, local_var not defined outside

# Modify global
def modify_global():
    global global_var
    global_var = 500

modify_global()
print(global_var)           # 500


# ===============================
# LAMBDA / ANONYMOUS FUNCTIONS
# ===============================

square = lambda x: x*x
print(square(5))

# Lambda in higher-order functions
nums = [1,2,3,4,5]
squared = list(map(lambda x: x**2, nums))
print(squared)


# ===============================
# HIGHER-ORDER FUNCTIONS
# ===============================

# Map
doubled = list(map(lambda x: x*2, nums))
print(doubled)

# Filter
evens = list(filter(lambda x: x%2==0, nums))
print(evens)

# Reduce
from functools import reduce
sum_all = reduce(lambda x, y: x+y, nums)
print(sum_all)


# ===============================
# RECURSION
# ===============================

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))


# ===============================
# DOCSTRINGS
# ===============================

def add_docs(a, b):
    """Returns sum of a and b"""
    return a + b

print(add_docs.__doc__)


# ===============================
# INTERVIEW TRICKS & TIPS
# ===============================

# 1. Mutable default argument trap
def append_to_list(val, lst=[]):
    lst.append(val)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2] ❌ usually unintended
# Fix:
def append_to_list2(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst

# 2. Function as object
def square(x): return x*x
f = square
print(f(5))

# 3. Functions can return functions
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
print(f(5))  # 15

# 4. Multiple return values
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([1,5,3,9])
print(low, high)

# 5. Swapping using function
def swap(a, b):
    return b, a

x, y = swap(5, 10)
print(x, y)

#--------------------------8[if-else]---------------------------
# ==========================================
# MULTIPLE CONDITIONS & COMBINATIONS
# ==========================================
x = 15
y = 20
z = 25

# Using multiple logical operators
if x < y < z:
    print("x < y < z")  # Chained comparison works in Python

# Using not, and, or together
a = True
b = False
if a and not b or (x > 10 and y < 25):
    print("Complex condition True")

# Nested ternary (inline if-else)
num = 10
res = "Even" if num % 2 == 0 else "Odd"
print(res)

# Multiple inline if-else chaining
num = 15
print("Zero" if num==0 else "Even" if num%2==0 else "Odd")


# ==========================================
# NESTED IF-ELSE
# ==========================================
score = 78
if score >= 50:
    if score >= 90:
        grade = "A+"
    elif score >= 75:
        grade = "A"
    else:
        grade = "B"
else:
    grade = "Fail"
print("Grade:", grade)


# ==========================================
# TRICKY SCENARIOS / INTERVIEW GOTCHAS
# ==========================================

# 1. Single-line if-else with print
a, b = 5, 10
print("A") if a > b else print("B")  # prints B

# 2. Chained comparison edge case
x, y = 5, 10
if 0 < x < 10 and 5 < y < 15:
    print("Both in range")  # True

# 3. Boolean as integer trick
flag = True
if flag == 1:
    print("Flag treated as int")  # True because True == 1

# 4. Multiple if vs if-elif difference
x = 10
if x > 5:
    print("x > 5")
if x > 0:
    print("x > 0")  # Both executed

x = 10
if x > 5:
    print("x > 5")
elif x > 0:
    print("x > 0")  # Only first executed


# ==========================================
# IF-ELIF-ELSE TRICKY BOUNDARY CASES
# ==========================================
marks = 85
if marks > 85:
    print("A+")
elif marks >= 85:  # boundary overlapping
    print("A")      # This executes
else:
    print("B")

# Float comparison
val = 0.1 + 0.2
if val == 0.3:
    print("Exact match")  # ❌ Won't execute due to floating-point precision
else:
    print("Use round() for float comparison")
print(round(val, 1) == 0.3)  # ✅ True

# Negative and zero checks
num = 0
if num:
    print("Non-zero")
else:
    print("Zero or False")  # Zero treated as False

# ==========================================
# NESTED TERNARY / COMPACT LOGIC
# ==========================================
x = 10
y = 20
z = 30
print("x max" if x>y and x>z else "y max" if y>z else "z max")  # prints z max

# ==========================================
# INTERVIEW TRICKS WITH IF
# ==========================================

# 1. Using 'is' vs '=='
a = [1,2,3]
b = [1,2,3]
if a == b:
    print("Equal")   # ✅ True, compares values
if a is b:
    print("Same")    # ❌ False, different objects

# 2. Truthy/falsy values in conditions
items = []
if items:  # Empty list treated as False
    print("Non-empty")
else:
    print("Empty")  # ✅ prints Empty

# 3. Nested if-else in one line
n = 15
print("Fizz" if n%3==0 else "Buzz" if n%5==0 else "FizzBuzz" if n%15==0 else n)

# 4. Complex logical evaluation order
a, b, c = 0, 1, 2
if a or b and c:  # and > or
    print("Tricky logic True")  # True because b and c => 2 => True, then a or True => True

# 5. Edge case: single '=' instead of '=='
# if a = 5:  # ❌ SyntaxError, can't assign in if
if (a := 5):  # ✅ Python 3.8+ walrus operator
    print("Assignment in if works", a)

# 6. Using 'in' and 'not in'
x = 5
if x in [1,2,3,4,5]:
    print("Found in list")
if x not in range(0,5):
    print("Not found in range")  # ❌ won't print

#--------------------------9loops---------------------------
# ==========================================
# 1. ITERATE WITH RANGE, STEPS, REVERSE
# ==========================================
for i in range(10, 0, -2):  # start, stop(exclusive), step
    print(i, end=' ')  # prints 10 8 6 4 2
print()

# Skipping elements
for i in range(0, 10, 3):
    print(i, end=' ')  # prints 0 3 6 9
print()


# ==========================================
# 2. ENUMERATE TRICKS
# ==========================================
fruits = ['apple', 'banana', 'cherry']
for idx, val in enumerate(fruits, start=1):  # start index from 1
    print(idx, val)


# ==========================================
# 3. NESTED FOR LOOPS — PATTERNS
# ==========================================
# Right-angled triangle
n = 4
for i in range(1, n+1):
    print('*' * i)

# Number pyramid
for i in range(1, n+1):
    for j in range(i):
        print(i, end='')
    print()

# Multiplication table (nested loop)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")


# ==========================================
# 4. BREAK & CONTINUE TRICKS
# ==========================================
nums = [10, 20, 30, 40, 50]

for n in nums:
    if n == 30:
        break  # stops loop completely
    print(n)  # prints 10,20

for n in nums:
    if n == 30:
        continue  # skips this iteration
    print(n)  # prints 10,20,40,50

# else with for loop (executes if loop is NOT broken)
for n in nums:
    if n == 100:
        print("Found")
        break
else:
    print("Not Found")  # ✅ prints "Not Found"


# ==========================================
# 5. ITERATE STRING, LIST, DICT, SET
# ==========================================
text = "Python"
for c in text:
    print(c, end=' ')
print()

d = {'a':1, 'b':2, 'c':3}
for k, v in d.items():
    print(k, v)

s = {10, 20, 30}
for val in sorted(s):  # sets are unordered, sorted ensures order
    print(val)


# ==========================================
# 6. INDEX WITHOUT ENUMERATE
# ==========================================
lst = [100, 200, 300]
for i in range(len(lst)):
    print(i, lst[i])


# ==========================================
# 7. TRICKY ITERATIONS / CONDITIONS
# ==========================================
# Find index of first occurrence
nums = [10, 20, 30, 40]
for idx, val in enumerate(nums, start=1):
    if val == 30:
        print("Found at:", idx)
        break

# Print until a condition and stop
letters = ['a','b','c','d','e']
for l in letters:
    if l == 'c':
        print("Found letter")
        break
    print(l)  # prints a b


# ==========================================
# 8. FOR LOOP SUM / PRODUCT
# ==========================================
nums = [1,2,3,4,5]

# sum
total = 0
for n in nums:
    total += n
print("Sum:", total)

# product
product = 1
for n in nums:
    product *= n
print("Product:", product)


# ==========================================
# 9. FOR LOOP WITH FUNCTION
# ==========================================
def square(n):
    return n*n

for i in nums:
    print(i, square(i))


# ==========================================
# 10. LIST COMPREHENSIONS TRICKY VERSION
# ==========================================
# Square numbers divisible by 2
squares = [x*x for x in nums if x%2==0]
print(squares)

# Nested loops in comprehension
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)  # [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]


# ==========================================
# 11. EDGE CASES / GOTCHAS
# ==========================================
# Using break in nested loops
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # breaks inner loop only
        print(i, j)

# Using continue in nested loops
for i in range(3):
    for j in range(3):
        if j == 1:
            continue  # skips iteration of inner loop only
        print(i, j)

# Empty list / string / dict
for x in []:
    print("Won't execute")  # ✅ safe, no error

for k,v in {}.items():
    print("Won't execute")  # ✅ safe, no error

#--------------------------10[while]---------------------------
# ===== 1. CLASS & INSTANCE BASICS =====
class Employee:
    company = "TechX"  # class attribute
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age

e1, e2 = Employee("Alice", 25), Employee("Bob", 30)
print(e1.name, e1.age, e1.company)  # Alice 25 TechX
Employee.company = "NewTech"
print(e1.company, e2.company)  # NewTech NewTech
e1.age = 26
print(e1.age, e2.age)  # 26 30


# ===== 2. METHODS & SELF =====
class Student:
    def __init__(self, name): self.name = name
    def greet(self): print(f"Hello, I am {self.name}")

s = Student("John")
s.greet()  # Hello, I am John
s.name = "JJ"
s.greet()  # Hello, I am JJ


# ===== 3. CLASS VS INSTANCE ATTRIBUTES =====
class Test: val = 0
t1, t2 = Test(), Test()
t1.val = 5  # overrides instance attribute
print(t1.val, t2.val, Test.val)  # 5 0 0
Test.val += 1
print(t1.val, t2.val, Test.val)  # 5 1 1


# ===== 4. PRIVATE / PROTECTED =====
class Bank:
    def __init__(self, bal): self.__bal = bal; self._id = 123

b = Bank(1000)
print(b._Bank__bal, b._id)  # 1000 123


# ===== 5. CLASS & STATIC METHODS =====
class Circle:
    pi = 3.14
    def __init__(self, r): self.radius = r
    @classmethod
    def set_pi(cls, new_pi): cls.pi = new_pi
    @staticmethod
    def area(r): return Circle.pi * r**2

c = Circle(5)
print(c.area(5))  # 78.5
Circle.set_pi(3)
print(Circle.area(5))  # 75


# ===== 6. INHERITANCE =====
class Animal: 
    def speak(self): print("Animal speaks")
class Dog(Animal): 
    def speak(self): print("Dog barks")
class Puppy(Dog): pass

Puppy().speak()  # Dog barks


# ===== 7. SPECIAL METHODS =====
class Vector:
    def __init__(self,x,y): self.x, self.y = x,y
    def __add__(self,o): return Vector(self.x+o.x, self.y+o.y)
    def __repr__(self): return f"Vector({self.x},{self.y})"

print(Vector(2,3)+Vector(5,7))  # Vector(7,10)


# ===== 8. COMPOSITION =====
class Engine: 
    def __init__(self,power): self.power = power
class Car: 
    def __init__(self, model, engine): self.model, self.engine = model, engine

c = Car("BMW", Engine(200))
print(c.model, c.engine.power)  # BMW 200


# ===== 9. EDGE CASES =====
class Demo: vals = []  # mutable class attribute
d1,d2 = Demo(),Demo()
d1.vals.append(1)
print(d2.vals)  # [1] shared!

class Demo2: 
    def __init__(self): self.vals = []
d1,d2 = Demo2(),Demo2()
d1.vals.append(1)
print(d2.vals)  # [] separate


# ===== 10. DYNAMIC ATTRIBUTES =====
c.color = "red"
print(c.color)
del c.color
# print(c.color)  # AttributeError

#--------------------------11[classes]---------------------------
# ===== 1. BASIC CLASS & OBJECT =====
class Employee:
    name = "John"
    age = 26

emp = Employee()
print(emp.name, emp.age)  # John 26

# ===== 2. METHODS =====
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Employee Name: {self.name}, Age: {self.age}")

emp1 = Employee("John", 26)
emp2 = Employee("Jane", 24)
emp1.details()
emp2.details()

# ===== 3. MODIFYING ATTRIBUTES =====
class Student:
    def __init__(self, name): self.name = name
    def intro(self): print("Hi I am", self.name)
    def change_name(self, name): self.name = name

john = Student('john')
john.intro()          # Hi I am john
john.change_name('JJ')
john.intro()          # Hi I am JJ

# ===== 4. METHODS RETURNING VALUES =====
class Rectangle:
    def __init__(self, length, width):
        self.length, self.width = length, width
    def area(self):
        print(f"Length - {self.length}, Width - {self.width}")
        return self.length * self.width

first = Rectangle(5,2)
print(first.area())  # 10

# ===== 5. ANOTHER EXAMPLE =====
class Dog:
    def __init__(self, breed, age, color):
        self.breed, self.age, self.color = breed, age, color
    def details(self):
        print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.color}")

dog1 = Dog('Husky', 5, 'Black')
dog1.details()
print(dog1.age)  # 5

# ===== 6. WHY USE CLASSES =====
# Without classes, for 500 students we’d need thousands of separate variables.
# Classes allow structured, reusable, and manageable code.

#--------------------------12[module]---------------------------
# ===== 1. IMPORTING MODULES =====
import math          # import entire module
from math import sqrt  # import specific function
print(dir(math))
# Using math module
print(math.sqrt(4))        # 2.0
print(sqrt(16))            # 4.0
print(math.log10(100))     # 2.0
print(math.pi)             # 3.141592653589793
print(math.sin(math.radians(90)))  # 1.0

# ===== 2. DATE & TIME MODULE =====
from datetime import date, datetime

today = date.today()
print(today)                     # e.g. 2026-01-03
print(today.day, today.month, today.year)  # 3 1 2026

now = datetime.now()
print(now)                        # e.g. 2026-01-03 19:30:45.123456
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2026-01-03 19:30:45

# ===== 3. MODULE VS PACKAGE =====
# - Module: single file of Python code (e.g., math.py)
# - Package: collection of modules (e.g., datetime package has date, datetime, time, etc.)

# ===== 4. SUMMARY =====
# - Modules help organize code and reuse functions
# - Import only what you need for cleaner code
# - math module: sqrt, log10, pi, sin, cos, etc.
# - datetime module: current date/time, formatting
