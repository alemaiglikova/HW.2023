def plus_two(number):
    try:
        result = number + 2
        print(result)
    except TypeError:
        print("Ожидаемый тип данных — число!")
#################################################
arr = [1, 2, 3]
index = 10

try:
    value = arr[index]
    print(value)
except IndexError:
    print("Индекс выходит за границы массива!")
