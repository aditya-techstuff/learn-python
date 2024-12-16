x = 'a value for x'
d = 20

strNum = int('12')

# many values to many variables
a, b, c = 'a', 'b', 20
print(a, b, c)

# many values to one variable
a = b = c = 'a'
print(a, b, c)

# Object definition
obj = { 'name': 'Aditya' }
print(obj)

# collections
fruits = ['apple', 'banana', 'cherry']
q,w,e = fruits

print(fruits)
print(q, w, e)


# global variable inside function
g1 = 'old value'

def myfunct():
  global g1
  print(g1)
  g1 = 'new value'

myfunct()
print(g1)



# type of variable
dict = 'test'
dict = 30
dict = { 'name': 'aditya' }
print(type(dict))

# list, tuple, set
list = [ 'a', 'b', 'c' ]
tuple = ( 'a', 'b', 'c' )
set = { 'a', 'b', 'c'  }

print(list, tuple, set)

import random

print(random.randrange(1, 10))