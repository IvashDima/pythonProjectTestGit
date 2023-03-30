
def farengeht (x):      # map task 1 farengeht
    return (x * 9 / 5) + 32
def farengeht_del (y):  # map task 1.1 farengeht_del_5
    return y / 5
def leng(x):            # map task 2 leng
    return len(x)
def upper_register(x):  # map task 3 upper_register
    return x.upper()

if __name__ == '__main__':
# map task 1 farengeht
    temp_cel = [0, 10, 20, 30, 40]
    print('celsius: ', temp_cel)
    temp_far = list(map(farengeht, temp_cel))
    print('farengeht: ', list(temp_far))
    temp_far_del_5_1 = map(farengeht_del, temp_far)
    print('farengeht/5 v1: ', list(temp_far_del_5_1))
    temp_far_del_5_2 = map(lambda y: y / 5, temp_far)
    print('farengeht/5 v2: ', list(temp_far_del_5_2))

# map task 2 leng
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    all_leng = map(leng, fruits)
    print('leng: ', list(all_leng))

# map task 3 upper_register
    list_rows = ['hello', 'world', 'python', 'programming']
    upper_list_rows = map(upper_register, list_rows)
    print('high_reg: ', list(upper_list_rows))