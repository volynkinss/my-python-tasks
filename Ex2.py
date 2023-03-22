# ex2 - sum two numbers
def get_elements_from_input(size):
    print("количество элементов в массиве " + str(size))
    list = []
    while len(list) < size:
        input_element = input("Введите число ")
        input_number = int(input_element)
        list.append(input_number)

    return list


try:
    element_count = input("Введи количество элементов в массиве ")
    element_count_size = int(element_count)
    array_of_elements = get_elements_from_input(element_count_size)
    result = sum(array_of_elements)
    print("Сумма введенных чисел равна ", result)
except ValueError:
    print("Необходимо вводить только целые числа")
except Exception as e:
    print("Произошла ошибка: ", e)
