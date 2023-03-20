# ex2 - sum two numbers
def array_creation(size):
    print ("количество элементов в массиве "  + str(size))
    list = []
    size_temp = int(size)
    while len(list) < size:
        number = input("Введите число ")
        number_int = int(number)
        list.append(number_int)

    return list


try:
   element_count = input("Введи количество элементов в массиве ")
   element_count_size = int(element_count)
   summ = array_creation(element_count_size)
   result = sum(summ)
   print("Сумма чисел введенных равна " , result)
except Exception as e:
        print("Необходимо вводить только числа")
        print(e)
