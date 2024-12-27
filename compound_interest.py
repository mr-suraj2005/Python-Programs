p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))
a = p*pow((1+(r/100)),t)
ci = a-p
print("Amount is: ",a)
print("Compound Interest is: ",ci)