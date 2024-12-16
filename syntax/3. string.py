
for x in 'banana':
  print(x)

text = 'this is a beautiful world!'
print('is' in text)
print('is' not in text)
print('eauti' in text)

if 'beautiful' in text:
  print('yes, it\'s beautiful!')

# replace
print('Hello World'.replace('l', 'D'))


# slicing values
print(text[0])
print(text[0:4])
print(text[:7])
print(text[2:])

# get upto world
print(text[-6:])
# get from world
print(text[:-6])

# array slicing
list = [1,2,3,4,5,6]

# last item
print(list[-1])

# before index 3
print(list[:2])

# after 3
print(list[2:])

print('===================== formatting =====================')
age = 32
print(f'Hello Aditya, you are {age} years old')
print(f'Next year you will be {age + 1}')
