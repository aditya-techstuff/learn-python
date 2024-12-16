# adding comments in python is easy
x = input('Enter a number: ')

print(x.isdigit())

if x.isdigit():
  x = int(x)
  print('x is a number... processing further')
  if x < 5:
    print('x is less than 5')
  elif x <= 10 and x >= 5:
    print('x is between 5 and 10')
  else:
    print('x is greater than 10')
