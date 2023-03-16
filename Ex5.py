#ex5 - multiplication table of the entered number
while True:
    try:
        num = int(input("Введите целое число: "))
        prod = list(range(1,11))
        for i,elem in enumerate(prod):
            prod[i] *=num
        print(prod)
        break
    except:
        print("Необходимо ввести одно целое число")
    