

# 1 2 3 4 5
# четное 10
# не четное 5
#def calc(x):
#    if x % 2 == 0:
#        return
#new_list = [1, 2, 3, 4, 5]
#print()
#print('even: ')
#print('not even: ')
def is_even(x):     # filter example
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print('is_even: ', list(even_numbers)) # [2, 4]


#def len_less_5(x): # filter task 1
#    if len(x) < 5:
#        return x

# filter task 1
#fruits = ['apple', 'banana', 'orange', 'kiwi']
#all_leng = map(len_less_5, fruits)
#print('len_less_5: ', list(all_leng))

from functools import reduce
def multiply(x, y): # reduce example
    return x * y
def sum(x, y): # reduce task 1
    return x + y

numbers = [1, 2, 3, 4, 5]
res_multi = reduce(multiply, numbers)
res_sum = reduce(sum, numbers)
print('reduce multiply: ', res_multi) #120
print('reduce sum: ', res_sum) #120

def biggest(x, y): # reduce task 2
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return false

numbers = [23, 12, 56, 34, 78, 9, 67]
result = reduce(biggest, numbers)
print('biggest element: ', result)

def is_positive(num): # without Lambda example
    return num >= 0

numbers = [-1, 2, -3, 4, -5]
positive_numbers = filter(is_positive, numbers)
print('without Lambda: ', list(positive_numbers)) # [2, 4]

numbers = [-1, 2, -3, 4, -5] # without Lambda example
positive_numbers = filter(lambda num: num >= 0, numbers)
print('with Lambda example: ', list(positive_numbers)) # [2, 4]

# zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = zip(names, ages)
print('zip: ', list(people)) # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# enumerate
fruits = ['apple', 'banana', 'cherry']
for index, fruits in enumerate(fruits):
    print('enumerate: ', index, fruits)

# sorted
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

