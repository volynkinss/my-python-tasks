#program for print multiplication table of number entered by the user
num = int(input())
#prod = [[num] for num in range(1,11)]
prod = list(range(1,11))
for i,elem in enumerate(prod):
        prod[i] *=num
print(prod)