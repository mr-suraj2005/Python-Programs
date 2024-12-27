a = int(input("Enter three digit number: "))
digit = a
sum = 0
while(a > 0) :
    temp = a % 10
    sum += temp
    a //= 10
if(digit == sum):
    print(digit,"is an Armstrong number")
else:
    print(digit,"is not an Armstrong number")