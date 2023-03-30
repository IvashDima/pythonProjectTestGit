#                LISTS                 #

# 1. Напишите функцию, которая будет возвращать True, если переданный в нее список отсортирован,
# или False, если он не отсортирован (по возрастанию, т.е. от меньшего к большему). Если в списке строки,
# то отсортированным он считается, когда элементы расположены по алфавиту.

def is_sorted(my_list):
    if my_list == sorted(my_list):
#        print('my_list, sorted: ', my_list, sorted(my_list))
        return True
    else:
#        print('my_list, sorted: ', my_list, sorted(my_list))
        return False


# 2. Напишите функцию, которая будет принимать список и переменную item и возвращать часть списка ДО первого места,
# где попался item.
# Пример: в функцию передан список [-1, 3, 2, 5, 1, 6] и item = 2. В таком случае ваша функция должна вернуть
# список [-1, 3]
# Если значение, равное item, стоит на первом месте списка, верните пустой лист [].
# Если значения, равного item, в списке не нашлось, верните строку "Error"

def get_sublist(my_list, item):
#    print('my_list, item: ', my_list, item)
    if item in my_list:  # my_list.index(item) =  :
        if my_list.index(item) == 0:
            return []
        else:
            return my_list[0:my_list.index(item)]
    else:
        return "Error"


#            DICTIONARIES                 #

# 3. В функцию передан dictionary, где ключи - немецкие города, а занчения - количество очков набранных этим городом
# в рейтинге удобства для жизни.
# Функция должна вернуть tuple, который содержит 3 элемента:
# 1) сумму очков всех городов
# 2) среднее арифметичское всех очков (сумма, деленная на количество элементов)
# 3) название города, у которого максимальное количество очков

def city_rating(cities_dict):
    sum_city_rating = sum(cities_dict.values())
#    print('sum_city_rating: ', sum_city_rating)
    average_rating = sum_city_rating/len(cities_dict)
#    print('average_rating: ', average_rating)
    for k, v in cities_dict.items():
        if v == max(cities_dict.values()):
            comf_living = k
#    print('comf_living: ', comf_living)
    return sum_city_rating, average_rating, comf_living


#                SETS                 #

# 4. Вам даны списки групп трех детских кружков: плавание (swimming), шахматы (chess) и игра на гитаре (guitar).
# Переданы эти данные в виде dictionary, где ключи - названия кружков, и значения - списки участников.
# Вам нужно вернуть множество детей, которые не знают никого, кроме одногруппников из своего кружка (то есть они
# не пересекаются с детьми из других кружков)

def not_busy_children(groups_dict):
    all_children = []
    for key in groups_dict.keys():
        for value in groups_dict[key]:
            all_children.append(value)
#    print('all_children: ', all_children)
    alone_children = set()
    for name in all_children:
        if all_children.count(name) <= 1:
           alone_children.add(name)
#           print('alone_children: ', alone_children)
    return alone_children

# ===========================================================================
# КОД НИЖЕ МЕНЯТЬ НЕЛЬЗЯ
# ===========================================================================

def test_is_sorted():
    assert is_sorted([1, 3, 5]) == True
    assert is_sorted([1, 5, 3, 8, 10]) == False
    assert is_sorted(["apple", "blackberry", "cherry", "plum"]) == True
    assert is_sorted(["mercedes", "mazda", "suzuki", "toyota"]) == False


def test_get_sublist():
    assert get_sublist([1, 3, 5], 1) == []
    assert get_sublist([1, 5, 3, 8, 10], 8) == [1, 5, 3]
    assert get_sublist([], 8) == "Error"
    assert get_sublist(["apple", "blackberry", "cherry", "plum"], "carrot") == "Error"
    assert get_sublist(["mercedes", "mazda", "toyota", "suzuki"], "mazda") == ["mercedes"]


def test_city_rating():
    cities_dict = {
        "Munich": 74,
        "Berlin": 62,
        "Cologne": 51,
        "Hamburg": 68,
        "Dusseldorf": 59,
        "Kassel": 52
    }
    assert city_rating(cities_dict) == (366, 61.0, "Munich")


def test_not_busy_children():
    groups = {
        "swimming": ["Emma", "Albert", "Peter"],
        "chess": ["Caroline", "Albert", "Pam", "Harry"],
        "guitar": ["Harry", "Peter", "Sam"],
    }
    assert not_busy_children(groups) == {"Emma", "Caroline", "Pam", "Sam"}


if __name__ == '__main__':
    test_is_sorted()
    test_get_sublist()
    test_city_rating()
    test_not_busy_children()
