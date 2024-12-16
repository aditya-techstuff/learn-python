thislist = ['apple', 'banana', 'orange']

if 'apple' in thislist:
  print('Yes, apple is a fruit!')

# turnary ?
print('chery is not a fruit' if 'cherry' not in thislist else 'cherry is a fruit')

# change range of items
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

list1 = ["apple", 'banana', 'cherry']
list2 = [1, 5, 7, 9, 3]
list1.extend(list2)
print(list1)

list2.extend(list1)
print(list2)

list1.remove('apple')
print(list1)

list1.pop(1)
print(list1)

# filter list (list comperhension)
new_list = [l for l in thislist if l not in ['apple', 'cherry']]
new_list_upper = [fruit.upper() for fruit in thislist if fruit not in ['apple', 'cherry']]
new_list_without_banana = [x if x != "banana" else "orange" for x in thislist]

# sort list
thislist.sort(key = str.lower)

def sort_custom(n):
  return abs(n-50)

[2,3,56,87].sort(key = sort_custom)

print('--------- Tuple ---------')
this_tuple = ('apple', 'banana', 'cherry')
print(this_tuple)
print(len(this_tuple))

(apple, banana, cherry) = this_tuple

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

i = 0
while i < len(fruits):
  print(f'index: {i} - {fruits[i]}')
  i = i + 1

print('--------- dictionary ---------')
person = {
  'name': 'aditya vaishnav',
  'age': 32
}