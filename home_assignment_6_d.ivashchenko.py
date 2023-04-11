# 2. Вам дается файл task2_input.txt, в нем лежит список. Каждый элемент на новой строке, и последняя строка - значение
# искомого элемента el.
# Напишите функцию, которая будет принимать имя этого файла, читать данные из него и создавать файл task2_output.txt,
# куда будет записывать часть списка ДО первого места, где попался el.
# Пример: в функцию передан файл с числами -1, 3, 2, 5, 1, 6, 2 (каждый с новой строки, здесь через запятую
# для краткости). В таком случае значение el - 2 (последняя строка), и ваша функция должна записать в файл
# список -1, 3 (каждый элемент с новой строки).
# Если значение, равное el, стоит на первом месте списка, запишите в файл слово "Empty".
# Если значения, равного el, в списке не нашлось, запишите в файл слово "Error"

def get_sublist(file_name):
    file = open(file_name, "r")
    input_data = []
    for line in file:
        input_data.append(int(line))
#    print(input_data)
    file.close()
    el = input_data.pop()
#    print(el)
    file = open("task2_output.txt", "w")
    if el in input_data:
        if input_data.index(el) == 0:
            return file.write("Empty")
        else:
#            print(input_data[0:input_data.index(el)])
            for i in input_data[0:input_data.index(el)]:
                file.write(str(i) + "\n")
            file.close()
    else:
         return file.write("Error")

# 3. В функцию передается CSV файл task3_input.csv, c заголовком city,score. Ниже в нем информация в
# виде "название города,кол-во балов" (делимитер - запятая).
# Функция должна вернуть CSV файл task3_output.csv следующего вида:
#     score_sum,avg_score,best_city
#     1,2,3
# где:
# 1 - сумма очков всех городов
# 2 - среднее арифметичское всех очков (сумма, деленная на количество элементов)
# 3 - название города, у которого максимальное количество очков

import csv
def city_rating(file_name):
    file = open(file_name, "r")
    header = file.readline()
#    print("header: ", header)
    input_data = {}
    for line in file:
        city, score = line.strip().split(",")
        dataline = city, int(score)
#        print("dataline: ", dataline)
        input_data.update({dataline})
#        print("input_data: ", input_data)
    file.close()
    score_sum = sum(input_data.values())        # score_sum
#    print('score_sum: ', score_sum)
    avg_score = score_sum/len(input_data)       # avg_score
#    print('avg_score: ', avg_score)
    for k, v in input_data.items():             # best_city
        if v == max(input_data.values()):
            best_city = k
#    print('best_city: ', best_city)
    file = open("task3_output.csv", "w")
    file.write("score_sum," + "avg_score," + "best_city" + "\n")
#   line2 = str(score_sum), str(avg_score), best_city
#    print(line2)
#    file.write(str(line2))
    file.write(str(score_sum) + ', ' + str(avg_score) + ', ' + str(best_city))
#    file.write('"' + str(score_sum) + '", ' + '"' + str(avg_score) + '", ' + '"' + str(best_city) + '"')
    return file.close()

# 4. Вам дается файл task4_input.csv с заголовком name,swimming,chess,guitar и контентом следующего вида:
# имя ребенка и через запятую три значения - 1, если ребенок посещает соответствующий кружок, 0 - если нет.
# Пример:
#     name,swimming,chess,guitar
#     Emma,1,0,0
# У Эммы 1 только в колонке swimming, следовательно, она посещает только плавание.
# На основе этих данных вам нужно вычислить детей, которые не знают никого, кроме одногруппников из своего кружка
# (то есть они не пересекаются с детьми из других кружков).
# Результат запишите в файл task4_output.txt, где каждое имя из вычисленного множества - на новой строке

def not_busy_children(file_name):
    file = open(file_name)
    header = file.readline()
    children_in_group = {}
    alone_children = set()
    for line in file:
        name, swimming, chess, guitar = line.strip().split(",")
        children_in_group[name] = int(swimming), int(chess), int(guitar)
    file.close()
#    print("children_in_group: ", children_in_group)

    file = open("task4_output.txt", "w")
    for key in children_in_group.keys():
        numb_activ = 0
        for value in children_in_group[key]:
            numb_activ = numb_activ + value
        if numb_activ <= 1:
            alone_children.add(key)
            file.write(key + "\n")
#            print('alone_children: ', alone_children)
        else:
            continue
    file.close()

    return alone_children


# ===========================================================================
# КОД НИЖЕ МЕНЯТЬ НЕЛЬЗЯ
# ===========================================================================

def get_result_list(file_name):
    output = open(file_name)

    result_list = []
    for line in output:
        result_list.append(line.strip())
    return result_list


def get_city_rating_result(file_name):
    output = open(file_name)

    # skip the header
    output.readline()

    result = output.readline().strip().split(",")
    return tuple(result)


def test_get_sublist():
    get_sublist("task2_input.txt")
    result_list = get_result_list("task2_output.txt")
    result_list = [int(item) for item in result_list]

    assert result_list == [1, 5, 3]


def test_city_rating():
    city_rating("task3_input.csv")
    result_list = get_result_list("task3_output.csv")
    result = tuple(result_list)

    assert result == ("366", "61.0", "Munich")


def test_not_busy_children():
    not_busy_children("task4_input.csv")
    result_list = get_result_list("task4_output.txt")
    result = set(result_list)

    assert result == {"Emma", "Caroline", "Pam", "Sam"}

if __name__ == '__main__':
    test_get_sublist()
    test_city_rating()
    test_not_busy_children()
    print("Well done!!!")
