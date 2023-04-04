
def farengeht (x):      # map task 1 farengeht
    return (x * 9 / 5) + 32
def farengeht_del (y):  # map task 1.1 farengeht_del_5
    return y / 5
def leng(x):            # map task 2 leng
    return len(x)
def upper_register(x):  # map task 3 upper_register
    return x.upper()
def len_less_5(x):      # filter task 1
    if len(x) < 5:
        return x
def empty_rows(x):      # filter task 2
    if x != '':
        return x
def without_a(x):       # filter task 3
    if x[0] != 'a':
        return x

from functools import reduce
def sum(x, y):  # reduce task 1
    return x + y
def biggest(x, y): # reduce task 2
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return false
def one_row(x, y):  # reduce task 3
    return x + ' ' + y

if __name__ == '__main__':
    # map task 1 farengeht
    temp_cel = [0, 10, 20, 30, 40]
    print('map task 1: celsius: ', temp_cel)
    temp_far = list(map(farengeht, temp_cel))
    print('map task 1: farengeht: ', list(temp_far))
    temp_far_del_5_1 = map(farengeht_del, temp_far)
    print('map task 1: farengeht/5 v1: ', list(temp_far_del_5_1))
    temp_far_del_5_2 = map(lambda y: y / 5, temp_far)
    print('map task 1: farengeht/5 v2: ', list(temp_far_del_5_2))

    # map task 2 leng
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    all_leng = map(leng, fruits)
    print('map task 2: leng value: ', list(all_leng))

    # map task 3 upper_register
    list_rows = ['hello', 'world', 'python', 'programming']
    upper_list_rows = map(upper_register, list_rows)
    print('map task 3: high_reg: ', list(upper_list_rows))

    # filter task 1
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    all_leng = filter(len_less_5, fruits)
    print('filter task 1: len_less_5: ', list(all_leng))

    # filter task 2
    non_standart_list = ['hello', '', 'world', 'python', '', 'programming']
    without_empty = filter(empty_rows, non_standart_list)
    print('filter task 2: list without empty rows: ', list(without_empty))

    # filter task 3
    fruits_a = ['apple', 'banana', 'orange', 'kiwi', 'grape', 'avocado']
    without_a_list = filter(without_a, fruits_a)
    print('filter task 3: list without a: ', list(without_a_list))

    numbers = [1, 2, 3, 4, 5]
    # reduce task 1
    res_sum = reduce(sum, numbers)
    print('reduce task 1: sum: ', res_sum) #15
    # reduce task 2
    numbers = [23, 12, 56, 34, 78, 9, 67]
    result = reduce(biggest, numbers)
    print('reduce task 2: biggest element: ', result)
    # reduce task 3
    list_of_rows = ['hello', 'world', 'python', 'programming']
    one_row_list = reduce(one_row, list_of_rows)
    print('reduce task 3: one_row_list: ', one_row_list)
