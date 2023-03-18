qunt = input("Введите необходимое количество чисел ")
num = list()
if (qunt and qunt.strip()):
    i = 1
    while i < (int(qunt)+1):
        num.append(input("Введите число "))
        i +=1
    print(num)
    i = len(num)
    sum = 0
    while i > 0:
        sum = sum + int(num.pop())
        i -= 1
    print(sum)
else: print("Поле не может быть пустым")
