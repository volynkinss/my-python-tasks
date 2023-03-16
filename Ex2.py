# ex2 - sum two numbers
while True:
    try:
        a = input("Введите первое число: ") #input 1st number
        b = input("Введите второе число: ") #input 2nd number
        if (a and a.strip()) and (b and b.strip()):
            c = float(a) + float(b) #calculate sum of 2 numbers
            print ("Сумма двух чисел равна", c) #print sum of number
        else: print("Поле не может быть пустым")
        break
    except:
        print("Необходимо вводить только числа")
