# ex2 - sum two numbers


# def get_elements_from_input(size):
#     print("количество элементов в массиве " + str(size))
#     list = []
#     while len(list) < size:
#         input_element = input("Введите число ")
#         input_number = int(input_element)
#         list.append(input_number)

#     return list


def get_array(*array_of_elements: list):
    try:
        #        array_of_elements = get_elements_from_input(array_size)
        result = sum(array_of_elements)
        print("Сумма введенных чисел равна ", result)
    except ValueError:
        print("Необходимо вводить только целые числа")
    except Exception as e:
        print("Произошла ошибка: ", e)


# def main():
#     get_array_size()


# if __name__ == "__main__":
#     main()

get_array(1, 2, 3, 4, 5)
