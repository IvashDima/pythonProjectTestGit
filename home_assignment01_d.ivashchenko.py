
#
# 1. Напишите функцию, которая принимает значения x, y
# и вычисляет результат (x+2)*(y-3)
# Примечание: Вы уже реализовали эту функцию на уроке.
# Просто перепишите код и убедитесь, что он проходит тесты
#
def evaluate(x, y):
    res = (x + 2) * (y - 3)
#    print(f'Result of function (x + 2) * (y - 3): {int(res)}')
    return res

#
# 2. Напишите функцию, которая принимает длину и ширину некого прямоугольника
# Функция возвращает True, если этот прямоугольник является квадратом, и False в противном случае
# Примечание 1: Прямоугольник является квадратом, если обе его стороны равны
# Примечание 2: Как известно, геометрическая фигура должна иметь сторону с длиной больше нуля.
# Верните False также в том случае, если квадрат с такими сторонами существовать не может
#
def is_square(width, length):
    if width == length and width > 0 and length > 0:
#        print('There is square')
        return True
    else:
#        print('There is NOT square')
        return False

#
# 3. Напишите функцию, которая принимает длину и ширину некого прямоугольника
# Функция вычисляет площадь данного прямоугольника
#
# Примечание: Прямоугольник не может иметь отрицательной размерности.
# Если длина или ширина меньше или равна нулю, то верните строку "Error"
# (обратите внимание на корректность написания и регистр!)
#
def square_area(width, length):
    square = width * length
    if width <= 0 or length <= 0:
        String = "Error"
    else:
        String = square
#    print(f'Square area is {String}')
    return String

####
# Код ниже этой строки изменять запрещено
####

def test_is_square():
    assert is_square(3, 5) == False
    assert is_square(5, 3) == False
    assert is_square(3, 3) == True
    assert is_square(3, 0) == False
    assert is_square(0, 30) == False
    assert is_square(-3, 3) == False
    assert is_square(-5, -5) == False

def test_square_area():
    assert square_area(3, 5) == 15
    assert square_area(5, 3) == 15
    assert square_area(0, 10) == "Error"
    assert square_area(0, -4) == "Error"
    assert square_area(-5, -4) == "Error"

def test_evaluation():
    assert evaluate(2, 3) == 0
    assert evaluate(2, 0) == -12
    assert evaluate(-7, -2) == 25

if __name__ == '__main__':
    test_is_square()
    test_square_area()
    test_evaluation()
