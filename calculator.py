num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
operation = input("enter btw +,-,/,**,*: ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "/" :      
    result = num1/num2
elif operation == "*":
    result = num1*num2
elif operation == '**':
    result = num1**num2
else:
    result = "invalid syntax error"
print(result)        