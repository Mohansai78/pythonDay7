# -*- coding: utf-8 -*-
"""Day7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ziTk4clEinF7kSsWGha2-QVAZneiyFDC
"""

#operators
arithmetic
logicla
assignemtn
relational

#bitwise operators
#&
a=5

b=4

a&b

x=6
y=2

x&y

6&2

6|2

a|b

#~

a

~a

#^ xor operator

a

b

5^4

#>>

a#---->0000 0101
#right shift is 0000 0001

a>>2

#left shift
a<<2#---0001 0100

5*2^2

2^2

a=[1,2,3,5]

5 in a

if 5 in a:
    print("5 is inside a")

4 in a

if 4 in a:
    print("4 is inside a")
else:
    print("4 is not inside a")

#identity operator
a=10
b=10

a is b #this is checking id

id(a)

id(b)

a==b #it is checking value

x=20
y=40

x is not y

x==y

2*(2+3)

2+2-2

(2+3)/2%6//6-2

2.5%6

2.5//6

2+3/4-(2*2**3)%4-3

2**3>>3+2^3

#pthon functions
1. builin function
2. module based or library based or package based functions
3. user defined furction
    to organize the code
    to eleiminate the code duplication
    reuse again and again.

import array
array.array("i",(1,2,3,3))

syntax of function:
    def function_name(paramaters):
        <statements>
        return value
    calling function name

def fun():
    pass

def fun():
    return "hello world"
    #print("hello world")
#driver code
#function calling
fun()

a+b

def add(a,b):#a, b are parameters
    c=a+b
    return c
add(10,10)#arguments

def add(a,b):#a, b are parameters
    return a+b
d=add(10,10)#arguments
print(d)

sum((10,20)) #builtin sum of elements

sum((20,20))

def add(a,b):#a, b are parameters
    c=a+b
    return c
add(20,20)#arguments

add(30,40)

add(50,60)

def fun1(a,b):
    return a+b
res =fun1(20,30)+20
print(res)#res is varible it is responsble for holding data

#function with default value

def fun2(name, age=30): #default value
    print(f'my name is {name}, and age is {age}')
fun2("ganesh")

def fun2(name, age=30):
    print(f'my name is {name}, and age is {age}')
fun2("ganesh",35)

def fun2(name, age=30, marks=65):
    print(f'my name is {name}, and age is {age} my marks {marks}')
fun2("ganesh",35,80)
fun2("shatish",25, 89)

#function with variable length argument:
def fun3(a,b):
    print(a,b)
fun3(12)
fun3(12,3)
fun3(1,2,3,4,5)

#function with variable length argument:
def fun3(a,b=90):
    print(a,b)
fun3(12)
fun3(12,3)
fun3(1,2,3,4,5)

#function with variable length argument:
def fun3(a,*b):
    print(a,b)
fun3(12)#result empty tuple
fun3(12,3)#b is 3
fun3(1,2,3,4,5) #b is tuple which having

#function with keyword argument

def fun4(**kwargs):#keywords arguments
    print(kwargs,type(kwargs))
fun4(name="ganesh",marks=30)

"""
(PA----->Positional argument
DA----->Default argument,
VA---->variable lenghth arguments,
KWA------>keyword arguments
)
"""

#using function take input a="1/2/3/4/h"
#expected [1,2,3,4,'h']

def split_string(a):
    b=[]
    for i in a.split('/'):
        if i.isdigit():
            b.append(int(i))
        else:
            b.append(i)
c=split_string("1/2/3/4/h")
print(b)

a="1/2/3/4/h"
b=[]
for i in a.split('/'):
    if i.isdigit():
        b.append(int(i))
    else:
        b.append(i)
print(b)

#pass by reference(sending actaul value) or pass by value(sending copy value)

#pythoon only pass by reference
def fun(x1):
    print("inside before appending",x1, id(x1))
    x1.append(30)
    print("after appending",x1,id(x1))
list1=[1,2,3]
fun(list1)
print("after calling appending",list1,id(list1))

#lambda functions
1. anynoumous function
2. simply single line statement
3. we can call fun name as a argumnt for other built in function

def add1(a,b):
    return a+b
add1(2,3)

a=lambda a,b:a+b

a(2,3)

#comprehnsion
list
set
dictionary
generator

list1=[1,2,3,4]
liat2=[]
for i in list1:
    if i%2==0:
        liat2.append(i)
print(liat2)

##list comprehnsion
syntax:
a=[statements(expression) for var in iterbale condition]

v=[x**2 for x in list1]
print(v)

list1*2



##set comprehnsion
syntax:
a={statements(expression) for var in iterable condition}

set1={1,2,3}
v={x+2 for x in set1 if 2 in set1}
print(v)

#enumerate
list1
for i in list1:
    dict(enumerate(i))

