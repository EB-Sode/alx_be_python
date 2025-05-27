num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = str(input("Choose the operation(+, -, *, /): "))

match operation:
    case '+' :
        result = num1 + num2
    case '-' : 
        result = num1 - num2
    case '*' :
        result = num1 * num2
    case '/' :
        if num1 == 0 or num2 == 0:
            result = "Cannot divide by 0"
        else:
            result = num1 / num2
    case _ :
        result = "Invalid operation"
print("The result is ",result)
