num1 = int(input("Enter starting range: "))
num2 = int(input("Enter ending range: "))
for num in range(num1+1,num2):
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
   if num == sum:
       print(num)
