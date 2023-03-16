# ex2 - sum two numbers
while True:
    try:
        a = float(input("Введите первое число: ")) #input 1st number
        b = float(input("Введите второе число: ")) #input 2nd number
        c = a+b #calculate sum of 2 numbers
        print ("Сумма двух чисел равна", c) #print sum of numbers
        break
    except:
        print("Необходимо вводить только числа")