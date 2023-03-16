#ex4 - sum of entered numbers
while True:
    try:
        nums = [int(x)for x in input("Введите несколько чисел через пробел: ").split()]
        amount = sum(nums)
        print(amount)
        break
    except: print("Необходимо вводить целые числа")