#program for print multiplication table of number entered by the user
while True:
    try:
        num = int(input("Введите целое число: "))
        prod = list(range(1,11))
        for i,elem in enumerate(prod):
            prod[i] *=num
        print(prod)
        break
    except:
        print("Необходимо ввести целое число")
    