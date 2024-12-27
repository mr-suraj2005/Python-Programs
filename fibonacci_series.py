# Fibonacci series = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# for ea sy understanding, the series starts with 0, 1 and the next number is the sum of the previous two numbers
# and just do swapping of previously added value and the next value
n = (int(input("Enter the number of terms: ")))
a = 0
b = 1
print(a)
print(b)
for i in range(n):
    c = a+b
    print(c)
    a = b
    b = c