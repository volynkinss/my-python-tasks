#create program that input list of numbers and calculate amount 
nums = [int(x)for x in input().split()]
amount = sum(nums)
print(amount)